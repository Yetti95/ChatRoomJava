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
			
			Handler handle = new Handler();
			String user = handle.getJSONRequestUser();
			Map<String, Socket> clientpair = new HashMap<String, Socket>();
			clientpair.put(user, client);
			
			if(connections.isEmpty()) {
				
				connections.add(clientpair);
				
			}
			else{
				for(int i = 0; i<=connections.size(); i++) {
			
					if(connections.get(i).containsKey(user)) {
						handle.userNameTaken();
					}
					else {
						connections.add(clientpair);
					}
				}	
			}
			
		} catch(Exception e) {
			
		}
	}
}//end of connection
