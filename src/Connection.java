import java.net.*;
import java.io.*;
import org.json.*;
import java.util.*;
//import java.nio.charset.StandardCharsets;


public class Connection implements Runnable
{
	public static final int BUFFER_SIZE = 2048;
	public static final int PORT = 1134;


	private Socket client;
	private List<Map<String, Socket>> connections;
	private Calendar date;
	
	public Connection(Socket client, List<Map<String, Socket>> connections) {
		this.client = client;
		this.connections = connections;
		date = Calendar.getInstance();
	}

    /**
     * This method runs in a separate thread.
     */
	public void run() {
		try {
			
			Handler handle = new Handler(client);
			String user = handle.getJSONRequestUser();
			Map<String, Socket> clientpair = new HashMap<String, Socket>();
			clientpair.put(user, client);
			
			if(connections.isEmpty()) {
				
				connections.add(clientpair);
				
			}
			else{
				for(int i = 0; i<=connections.size(); i++) {
			
					if(connections.get(i).containsKey(user)) {
						//this needs to send back a error code for username taken and close the connect
						handle.userNameTaken();
					
					}
					else {
						connections.add(clientpair);
					}
				}	
			}
					
			if(handle.dm()) {
				handle.sendDM();
			}
			else if(handle.hasMessage()){
				sendMessage(handle.getJSONObject());
			}
				
//				handle.messageNotSent();

			
			
			
			
		} catch(Exception e) {
			System.out.println("failed to connect to the server in the connection class");
		}
		
		
	}

	private void sendMessage(Object jsonObject) throws IOException {
		// TODO Auto-generated method stub
		
		//this is not what we will end up using
		//BroadcastThread bt = new BroadcastThread();
		//bt.send(jsonObject);
		//^ is closer to what it will look like
		BufferedOutputStream outStream = new BufferedOutputStream(client.getOutputStream());
		byte[] byteStream = jsonObject.toString().getBytes();
		outStream.write(byteStream);
		outStream.flush();
		outStream.close();
		
	}
	
	
}//end of connection
