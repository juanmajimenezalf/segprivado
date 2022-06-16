import { Component } from '@angular/core';
import { ServicesService } from '../services/services.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  medicos: any[] = []
  citas: any[] = []
  medico_id: number

  constructor(private services: ServicesService) {}

  ngOnInit() {
    this.obtenerMedicos()
  }

  obtenerCitas(event){
    this.medico_id = event.target.value
    this.services.obtenerCitas().then(data => {
      this.citas = data
      this.citas = this.citas.filter(cita => cita.idMedico.id === this.medico_id)
      console.log(this.citas)
      console.log(this.medico_id)
    })

  }

  obtenerMedicos(){
    this.services.obtenerMedicos().then(data => {
      this.medicos = data
    })
  }

}
