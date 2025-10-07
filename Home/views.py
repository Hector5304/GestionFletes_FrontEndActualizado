from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date, timedelta

from IngresosEgresos.models import Ingresos, Egresos
from CrudRecorridos.models import Recorridos
from IngresosEgresos.models import Ingresos, Egresos as EgresosModel


@login_required
def home(request):
    # Último Ingreso
    ultimo_ingreso = Ingresos.objects.order_by('-fecha').first()
    ultimo_ingreso_val = ultimo_ingreso.valor if ultimo_ingreso else 0
    ultimo_ingreso_fecha = ultimo_ingreso.fecha if ultimo_ingreso else None

    # Último Egreso
    ultimo_egreso = Egresos.objects.order_by('-fecha').first()
    ultimo_egreso_val = ultimo_egreso.valor if ultimo_egreso else 0
    ultimo_egreso_fecha = ultimo_egreso.fecha if ultimo_egreso else None

    # Ingreso semanal (últimos 7 días)
    today = date.today()
    week_ago = today - timedelta(days=6)
    ingresos_semana_qs = Ingresos.objects.filter(fecha__range=(week_ago, today)).aggregate(total=Sum('valor'))
    ingresos_semana = ingresos_semana_qs['total'] or 0

    # Egreso semanal (últimos 7 días)
    egresos_semana_qs = Egresos.objects.filter(fecha__range=(week_ago, today)).aggregate(total=Sum('valor'))
    egresos_semana = egresos_semana_qs['total'] or 0

    context = {
        'ultimo_ingreso_val': ultimo_ingreso_val,
        'ultimo_ingreso_fecha': ultimo_ingreso_fecha,
        'ultimo_egreso_val': ultimo_egreso_val,
        'ultimo_egreso_fecha': ultimo_egreso_fecha,
        'ingresos_semana': ingresos_semana,
        'egresos_semana': egresos_semana,
    }

    # Preparar series diarias para la última semana (7 días: desde week_ago hasta today)
    labels = []
    ingresos_series = []
    egresos_series = []
    for i in range(7):
        day = week_ago + timedelta(days=i)
        labels.append(day.strftime('%a %d'))
        ingresos_val = Ingresos.objects.filter(fecha=day).aggregate(total=Sum('valor'))['total'] or 0
        egresos_val = Egresos.objects.filter(fecha=day).aggregate(total=Sum('valor'))['total'] or 0
        # Asegurar tipo serializable
        ingresos_series.append(float(ingresos_val))
        egresos_series.append(float(egresos_val))

    # Pasar como listas serializables a la plantilla
    context['trend_labels'] = labels
    context['trend_ingresos'] = ingresos_series
    context['trend_egresos'] = egresos_series
    # Últimos recorridos (resumen) - mostrar los 5 más recientes
    recent_recorridos_qs = Recorridos.objects.order_by('-fecha')[:5]
    # Mapear a lista de dicts livianos para la plantilla
    recent_recorridos = []
    for r in recent_recorridos_qs:
        recent_recorridos.append({
            'id': r.recorridoID,
            'fecha': r.fecha,
            'conductor': str(r.conductor),
            'origen': r.direccionOrigen,
            'destino': r.direccionDestino,
            'distancia_km': r.distancia_km,
            'carga': (r.carga[:60] + '...') if r.carga and len(r.carga) > 60 else (r.carga or '')
        })

    context['recent_recorridos'] = recent_recorridos

    # Últimas transacciones: combinar Ingresos y Egresos por fecha
    recent_transactions = []
    # Traer 5 últimos ingresos y 5 últimos egresos, luego mezclar y ordenar por fecha desc
    ingresos_qs = Ingresos.objects.order_by('-fecha')[:5]
    egresos_qs = EgresosModel.objects.order_by('-fecha')[:5]

    for i in ingresos_qs:
        recent_transactions.append({
            'valor': i.valor,
            'tipo': 'Ingreso',
            'fecha': i.fecha,
            'recorrido': (f"{i.recorrido.direccionOrigen} → {i.recorrido.direccionDestino}" if i.recorrido else '—')
        })
    for e in egresos_qs:
        recent_transactions.append({
            'valor': e.valor,
            'tipo': 'Egreso',
            'fecha': e.fecha,
            'recorrido': (f"{e.recorrido.direccionOrigen} → {e.recorrido.direccionDestino}" if e.recorrido else '—')
        })

    # Ordenar por fecha desc y dejar los 5 más recientes
    recent_transactions = sorted(recent_transactions, key=lambda x: x['fecha'], reverse=True)[:5]
    context['recent_transactions'] = recent_transactions

    return render(request, 'home.html', context)