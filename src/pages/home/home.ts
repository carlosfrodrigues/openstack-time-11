import { Component, ElementRef, ViewChild } from '@angular/core';
import { NavController } from 'ionic-angular';
import {Geolocation } from '@ionic-native/geolocation';


declare var google: any;

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
map:any;

//revisar esse comando
@ViewChild('map') mapRef: ElementRef; 

  constructor(public navCtrl: NavController, private geolocation: Geolocation) {    
  }

  latitude:number;
  longitude:number;

  usuario:any; 
  
  ionViewDidLoad() { 
    this.geolocation.getCurrentPosition().then((resp) => {
      console.log("1")
      let location_2 = new google.maps.LatLng(resp.coords.latitude,resp.coords.longitude)
      
      const options = {
        center: location_2,
        zoom: 16,
        streetViewControl: false,
        fullscreenControl: false
      }
      console.log("3")
      this.showMap(options);
      this.usuario = this.markerPosition(location_2, this.map);
      this.usuario.title  = "teste"
      console.log(this.usuario)
      console.log("2")
      this.longitude = resp.coords.longitude;

     }).catch((error) => {
       console.log('Error getting location', error);
       const location_cristo = new google.maps.LatLng(-22.951916,-43.2126759)

       const options = {
        center: location_cristo,
        zoom: 16,
        streetViewControl: false,
        fullscreenControl: false
      }
      console.log("2")
       this.showMap(options);
       this.addMarker(location_cristo, this.map, false)
     });

     this.geolocation.watchPosition().subscribe((resp) => {
        this.usuario.setMap(null);

        var location_2 = new google.maps.LatLng(resp.coords.latitude,resp.coords.longitude);

        console.log(resp.coords.latitude,resp.coords.longitude);
        
        this.usuario = this.markerPosition(location_2, this.map);

        google.maps.event.addListener(this.usuario, 'click', function () {
          
          Infowindow.setContent(place.name);
          Infowindow.open(Map, this);  
        });
       });    
  }

  showMap(options:any) {
    console.log("1")
    //const location = new google.maps.LatLng(-21.92011,-43.256247)  
    //const location_3 = new google.maps.LatLng(-21.93011,-43.256247)
    const location_4 = new google.maps.LatLng(-22.93011,-43.226247)
    
    this.map = new google.maps.Map(this.mapRef.nativeElement, options);

    //this.addMarker(location, this.map, true)
    //this.addMarker(location_3, this.map, false)
    this.addMarker(location_4, this.map, false)
    
  }

addMarker(position, map, fixed:boolean) {

    var marker = new google.maps.Marker({
    position,
    draggable: fixed,
    map
  });
  return marker;
  }

markerPosition(position, map) {
  return new google.maps.Marker({
    position,
    draggable: true,
    map
  });
  //return marker;
}


}
