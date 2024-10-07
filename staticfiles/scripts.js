class AddFieldFormset{
	/*
	*@param {addButton} id del boton adherir
	*@param {formset} id del contenedor del formset
	*@param {extraFieldHTML} html del la fila extra
	*/
	constructor(addButton,formset,extraFieldHTML){
		this.addButton = document.getElementById(addButton);
		this.formset = document.getElementById(formset);
		this.extraFieldHTML = extraFieldHTML
		this.init()
	}
	init(){
		let instance = this;
		this.addButton.onclick = function(event){
			event.preventDefault();
			instance.addField();
		}
	}
	addField(){
		let total = this.formset.querySelector('[name$="_set-TOTAL_FORMS"]');
		let data = this.extraFieldHTML.replace(/__prefix__/g, total.value);
		total.value = parseInt(total.value) + 1;
		let parser = new DOMParser();
		data = document.createRange().createContextualFragment(data);
		this.formset.appendChild(data);
		//retorna el elemento creado o adeherido
		let res = this.formset.querySelectorAll('div.row');
		return res[res.length - 1];
	}
}