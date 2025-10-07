(function () {
  const btnEliminacion = document.querySelectorAll(".btnEliminacion");

  btnEliminacion.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const confirmacion = confirm("¿Esta seguro de eliminar el Vehiculo?");
      if (!confirmacion) {
        e.preventDefault();
      }
    });
  });
})();

// Form validations for Add New Car
(function(){
  const form = document.getElementById('vehiculoForm');
  if(!form) return;

  function showError(el, msg){
    el.classList.add('is-invalid');
    let feed = el.nextElementSibling;
    if(!feed || !feed.classList || !feed.classList.contains('invalid-feedback')){
      feed = document.createElement('div');
      feed.className = 'invalid-feedback';
      el.parentNode.appendChild(feed);
    }
    feed.textContent = msg;
  }

  function clearError(el){
    el.classList.remove('is-invalid');
    const feed = el.parentNode.querySelector('.invalid-feedback');
    if(feed) feed.textContent = '';
  }

  form.addEventListener('submit', function(e){
    let valid = true;
    // Patente validation (allow patterns like AA-229-DB or 6 alphanumeric)
    const patente = form.querySelector('[name="patente"]');
    if(patente){
      const val = patente.value.trim();
      const re = /^[A-Z0-9-]{4,10}$/i;
      if(!val){ showError(patente, 'La patente es obligatoria'); valid=false; }
      else if(!re.test(val)){ showError(patente, 'Formato de patente inválido'); valid=false; }
      else clearError(patente);
    }

    const marca = form.querySelector('[name="marca"]');
    if(marca){ if(!marca.value.trim()){ showError(marca,'La marca es obligatoria'); valid=false } else clearError(marca) }

    const modelo = form.querySelector('[name="modelo"]');
    if(modelo){ if(!modelo.value.trim()){ showError(modelo,'El modelo es obligatorio'); valid=false } else clearError(modelo) }

    const fecha = form.querySelector('[name="fechaAdquisicion"]');
    if(fecha){ if(!fecha.value){ showError(fecha,'La fecha es obligatoria'); valid=false } else clearError(fecha) }

    if(!valid) e.preventDefault();
  });

  // Image preview
  const fileInput = form.querySelector('input[type="file"][name="images"]');
  if(fileInput){
    const previewBox = document.createElement('div');
    previewBox.className = 'mt-2 d-flex gap-2 flex-wrap';
    fileInput.parentNode.appendChild(previewBox);

    fileInput.addEventListener('change', (ev)=>{
      previewBox.innerHTML = '';
      Array.from(ev.target.files).slice(0,6).forEach(file=>{
        if(!file.type.startsWith('image/')) return;
        const img = document.createElement('img');
        img.style.width = '120px'; img.style.height = '80px'; img.style.objectFit='cover'; img.style.borderRadius='6px';
        const reader = new FileReader();
        reader.onload = e => img.src = e.target.result;
        reader.readAsDataURL(file);
        previewBox.appendChild(img);
      })
    })
  }

})();
