import java.net.*;
import java.io.*;
import org.json.*;
import java.util.Calendar;
import java.util.List;
import java.util.Map;
import java.nio.charset.StandardCharsets;


public class Connection implements Runnable
{
	public static final int BUFFER_SIZE = 2048;
	public static final int PORT = 1134;


	private Socket client;
	private List<Map<String, Socket>> connections;
	//private Pair[] con;

	public Connection(Socket client, List<Map<String, Socket>> connections) {
		this.client = client;
		this.connections = connections;
	}

    /**
     * This method runs in a separate thread.
     */
	public void run() {
		try {
			Handler handle = new Handler();
			String user = handle.getJSONRequestUser();
			Map<String, Socket> clientpair = null;
			//			Map<String, Socket> clientpair = (Map<String, Socket>) clientpair.put(user, client);
			clientpair.put(user, client);
			if(connections.isEmpty()) {
//				Map<String, Socket> clientpair = new Map<String, Socket>();
				connections.add(clientpair);
				
			}
			else{
				for(int i = 0; i<=connections.size(); i++) {
			
					if(connections.contains(user)) {
						handle.userNameTaken();
					}
					else {
						connections.add(clientpair);
					}
				}
//			if(!connections.contains(user)) {
//				Map<String, Socket> clientPair = new Map<U>
//				connections.add(new Map<user, client>)
//			}
//			else {
//				
			}
			
		} catch(Exception e) {
			
		}
	}
}//end of connection
