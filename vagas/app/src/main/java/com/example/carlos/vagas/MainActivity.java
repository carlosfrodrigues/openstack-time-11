package com.example.carlos.vagas;

import android.Manifest;
import android.content.Context;
import android.location.Criteria;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Toast;

import com.github.clans.fab.FloatingActionButton;
import com.github.clans.fab.FloatingActionMenu;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

import java.net.URI;
import java.net.URISyntaxException;

public class MainActivity extends AppCompatActivity implements LocationListener, OnMapReadyCallback, GoogleMap.OnInfoWindowClickListener, GoogleMap.OnMarkerClickListener {
  public Marker marcardor;
  private LocationManager locationManager;
  private String provider;
  private String usuario_marker_title = "Adicionar Vaga";
  private Websocket ws;
  private GoogleMap mMap;
  private boolean map_is_ready = false;
  private boolean update_user_marker = true;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    ask_permission();

    try {
      ws = new Websocket(new URI("ws://10.20.3.197:40000"), this);
      ws.connect();

    } catch (URISyntaxException e) {
      e.printStackTrace();
    }

    // Obtain the SupportMapFragment and get notified when the map is ready to be used.
    SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
      .findFragmentById(R.id.map);
    mapFragment.getMapAsync(this);

    locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);

    Criteria criteria = new Criteria();
    provider = locationManager.getBestProvider(criteria, false);

    System.out.println("vagas location provider: " + provider);

    boolean enabled = locationManager
      .isProviderEnabled(LocationManager.GPS_PROVIDER);
  }

  @Override
  protected void onResume() {
    super.onResume();

    locationManager.requestLocationUpdates(provider, 0, 0, this);
  }

  @Override
  protected void onPause() {
    super.onPause();
    locationManager.removeUpdates(this);
  }

  private void ask_permission() {
    int permissionCheck = ContextCompat.checkSelfPermission(this,
      Manifest.permission.ACCESS_FINE_LOCATION);

//        if(permissionCheck > 0){
    ActivityCompat.requestPermissions(this,
      new String[]{Manifest.permission.ACCESS_FINE_LOCATION},
      1);

    ActivityCompat.requestPermissions(this,
      new String[]{Manifest.permission.ACCESS_COARSE_LOCATION},
      1);

//        }
  }

  public void imprimir() {
    System.out.println("JJJJJJJJJJJJJJJJJJJJ");
  }

  public void imprimir2() {
    System.out.println("YYYYYYYYYYYYYYYYYYYYYYYYY");
  }


  @Override
  public void onLocationChanged(Location location) {
    if (marcardor != null && update_user_marker) {
      marcardor.remove();
    }
    String msg = "Updated Location: " +
      Double.toString(location.getLatitude()) + "," +
      Double.toString(location.getLongitude());

    // You can now create a LatLng Object for use with maps
    LatLng latLng = new LatLng(location.getLatitude(), location.getLongitude());

    if (map_is_ready && update_user_marker) {
      marcardor = mMap.addMarker(new MarkerOptions().position(latLng).title(usuario_marker_title));

      mMap.moveCamera(CameraUpdateFactory.newLatLng(latLng));
      marcardor.setPosition(latLng);
    }
  }

  public void popularVagas(String msg) {

    try {
      String dados[] = msg.split(";");

      int n = 0;

      while (n < dados.length) {
        final LatLng latLng1 = new LatLng(Double.parseDouble(dados[n + 1]), Double.parseDouble(dados[n + 2]));

        runOnUiThread(new Runnable() {
          @Override
          public void run() {
            mMap.addMarker(new MarkerOptions().position(latLng1).title("Vaga!").icon(BitmapDescriptorFactory.fromResource(R.drawable.marker)));
          }
        });

        n = n + 6;
      }
    } catch (Exception e) {
      e.printStackTrace();
      System.out.println("DEU ERRADO DEU ERRADO");
    }

  }

  @Override
  public void onMapReady(GoogleMap googleMap) {
    Location location = new Location(provider);
    location.getLatitude();

    mMap = googleMap;
    map_is_ready = true;

    mMap.setOnInfoWindowClickListener(this);
    mMap.setOnMarkerClickListener(this);

    LatLng initial_pos = new LatLng(-22.893999, -43.295744);
    mMap.moveCamera(CameraUpdateFactory.newLatLng(initial_pos));
    mMap.animateCamera(CameraUpdateFactory.zoomTo(14));
  }

  @Override
  public void onStatusChanged(String s, int i, Bundle bundle) {

  }

  @Override
  public void onProviderEnabled(String s) {

  }

  @Override
  public void onProviderDisabled(String s) {

  }

  public void marcarLocal() {
    // PEGAR A LOCALIZAÇAO
    // Converrter para string
    ws.send("add_vaga" + "STRING CONVERTIDA");
  }

  public void positivarVaga() {
    // PEGAR A LOCALIZAÇAO DA VAGA
    // Converrter para string
    ws.send("positivar_vaga" + "STRING CONVERTIDA");
  }

  public void negativarVaga() {
    // PEGAR A LOCALIZAÇAO DA VAGA
    // Converrter para string
    ws.send("negativar_vaga" + "STRING CONVERTIDA");
  }


  @Override
  public void onInfoWindowClick(Marker marker) {
    if(marker.getTitle().equals(usuario_marker_title)){
      LatLng pos = marker.getPosition();

      ws.send("add_vagas<&>" + String.valueOf(pos.latitude) + ";" + String.valueOf(pos.longitude));

      marker.hideInfoWindow();

      update_user_marker = true;
    }
    else{
      System.out.println("vaga cadastrada");

//      marker.hideInfoWindow();
//      marker.remove();
    }
  }

  @Override
  public boolean onMarkerClick(Marker marker) {
    update_user_marker = false;

    return false;
  }

  public void show_feedback(final String msg){
    runOnUiThread(new Runnable() {
      @Override
      public void run() {
        Toast.makeText(getApplicationContext(), msg, Toast.LENGTH_SHORT).show();

        if(msg.equals("Vaga adicionada")){
          ws.send("todas_vagas");
        }
      }
    });
  }
}
