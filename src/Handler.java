import java.io.*;
import java.net.Socket;
import java.util.Date;

import org.json.*;


public class Handler {
	private JSONObject json;
	private Socket client;
	private BufferedInputStream in;
	private BufferedOutputStream out;
	private String username;
	private boolean isConnected;
	private String errorMessage; // this may be replaced by error codes
	private String[] dm;
	private String message;
	private int length;
	private Date currUTC; //Format YYYY-MM-DD-HH-MM-SS
	private boolean disconnect;
	
	/*
	 * I'm not sure if this JSONObject has what we want
	 * it only reads from files and not byte streams
	 */
	public Handler(Socket client) {
		this.client = client;
		try {
			in = new BufferedInputStream(client.getInputStream());
			out = new BufferedOutputStream(client.getOutputStream());
			byte[] byteStream = in.readAllBytes();
			JSONTokener token = new JSONTokener(in.read());
			json = JSONObject.wrap(temp);
			
			//set to JSONObject based off key pairs
			username = ""; 
			isConnected = true;
			errorMessage = "";
			//sets max group dm size to 10
			dm = new String[10];
			message = "";
			length = 0;
			disconnect = false;
			
		}
		catch (IOException e){
			System.out.println("failed to initialize BufferedStream");
		}
	}




	//Getters
	public String getJSONRequestUser() {
		// TODO Auto-generated method stub
		return username;
	}
	
	public JSONObject getJSONObject() {
		// TODO Auto-generated method stub
		return json;
	}

	
	public boolean isConnected() {
		return isConnected;
	}
	
	public String getErrors() {
		
		return errorMessage;
	}
	
	public String[] getDMS() {
		return dm;
	}
	
	public String getMessage() {
		return message;
	}
	
	public int getLength() {
		return length;
	}
	
	public String getDate() {
		StringBuilder stringBuilder = new StringBuilder();
		stringBuilder.append(currUTC.getYear());
		stringBuilder.append("-");
		stringBuilder.append(currUTC.getMonth());
		stringBuilder.append("-");
		stringBuilder.append(currUTC.getDay());
		stringBuilder.append("-");
		stringBuilder.append(currUTC.getHours());
		stringBuilder.append("-");
		stringBuilder.append(currUTC.getMinutes());
		stringBuilder.append("-");
		stringBuilder.append(currUTC.getSeconds());
		//Format YYYY-MM-DD-HH-MM-SS
		String date = new String(stringBuilder.toString());
		return date;
	}
	
	
	//checkers
	public boolean dm() {
		// TODO Auto-generated method stub
		boolean dming;
		if(dm.length == 0) {
			dming = true;
		}
		else {
			dming = false;
		}
		return dming;
	}
	
	public boolean hasMessage() {
		// TODO Auto-generated method stub
		// if contains key Message, value != null send true
		
		return false;
	}

	
	//Setters and doers
	public void userNameTaken() {
		// TODO Auto-generated method stub
		//error code send and close connections
	}
	
	public void closeConnection() {
		//may have change the client single length on enter json
		//if we include a connect bool then we could you that to signal that you are no longer connected
		String dcReturn = new String("{  add return" + "'tab' \" errorCode \" : " + "\"some int that means something\"");
		JSONObject returnDC = new JSONObject(dcReturn);
		client.sendShit(returnDC);
		client.close();
	}



	public void messageNotSent() {
		// TODO Auto-generated method stub
		
	}

	

	
	public void sendDM() {
		// TODO Auto-generated method stub
		//Construct the JSONObject to send
		
	}




}
