import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AlertController } from '@ionic/angular';

@Injectable({
  providedIn: 'root'
})
export class ServicesService {

  apiURL = 'http://127.0.0.1:8000/api';
  data_user: any;

  constructor(private http: HttpClient, private alertController: AlertController) { }

  async login(username, password) {
    return await new Promise<any>(reslove => {
      this.http.post(this.apiURL + '/login/', 
      { user: username,
        password: password
      })
        .subscribe(data => {
          this.data_user = data;
          console.log(this.data_user);
          reslove(data);
        }, async err => {
          console.log(err);
          const alert = await this.alertController.create({
            header: 'Fallo al iniciar sesión',
            message: 'El usuario o la contraseña son incorrectos',
            buttons: ['OK']
        });
        await alert.present();
        return;
      });
    });
  }

  async obtenerMedicos(){
    return await new Promise<any>(reslove => {
      this.http.get(this.apiURL + '/medicos/',{
        headers: new HttpHeaders().set('Authorization', 'Token ' + this.data_user.token)
      })
        .subscribe(data => {
          console.log(data);
          reslove(data);
        }, err => {
          console.log(err);
        });
    })
  }

  async obtenerCitas(){
    return await new Promise<any>(reslove => {
      this.http.get(this.apiURL + '/citas/',{
        headers: new HttpHeaders().set('Authorization', 'Token ' + this.data_user.token)
      })
        .subscribe(data => {
          console.log(data);
          reslove(data);
        }, err => {
          console.log(err);
        });
    })
  }
}
