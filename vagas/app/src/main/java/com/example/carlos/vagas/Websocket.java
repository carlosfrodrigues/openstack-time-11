package com.example.carlos.vagas;

import android.widget.Toast;

import org.java_websocket.WebSocket;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;

import java.net.URI;
import java.util.Objects;

/**
 * Created by carlos on 02/12/17.
 */

public class Websocket extends WebSocketClient {
  public Websocket(URI serverUri, MainActivity cpx) {
    super(serverUri);
    main = cpx;
  }

  private String message;
  public MainActivity main;

  @Override
  public void onOpen(ServerHandshake handshakedata) {
    System.out.println("opened connection");
    send("todas_vagas");


  }

  @Override
  public void onMessage(String message) {
    String msg[] = message.split("<&>");

    if (msg[0].equals("todas_vagas")) {

      main.popularVagas(msg[1]);

    }
    else if(msg[0].equals("feedback")){
     main.show_feedback(msg[1]);
    }

    this.message = message;

  }

  @Override
  public void onClose(int code, String reason, boolean remote) {
    // The codecodes are documented in class org.java_websocket.framing.CloseFrame
    System.out.println("Connection closed by " + (remote ? "remote peer" : "us") + " Code: " + code + " Reason: " + reason);
  }

  @Override
  public void onError(Exception ex) {
    ex.printStackTrace();
    // if the error is fatal then onClose will be called additionally
  }


}
