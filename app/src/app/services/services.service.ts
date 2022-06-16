import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AlertController } from '@ionic/angular';

@Injectable({
  providedIn: 'root'
})
export class ServicesService {

  apiURL = 'http://localhost:8000/api';
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
}
