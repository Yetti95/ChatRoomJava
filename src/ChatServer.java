import java.net.*;
import java.io.*;
import java.util.List;
import java.util.Map;
import java.util.concurrent.*;

public class ChatServer {
	//JSON datagram;
    //private Socket[] connections;
    public static final int DEFAULT_PORT = 1134;
    private static final Executor exec = Executors.newCachedThreadPool();
    
    
    //check server socket object to see what it acutally creates
    //is it another link to the client or does it open a port to listen to
    //should the server socket try to connect in the while?
    //PRESISTENT CONNECTIONS NEEDED
    
    public static void main(String args[]){
    	List<Map<String, Socket>> connections = null;
        while(true){
        
        	//Socket[] connections = new Socket[30];
            try{
            	
                ServerSocket server = new ServerSocket(DEFAULT_PORT);               
                System.out.println("Waiting for connections ....");
                Socket client = server.accept();                           
                Connection connection = new Connection(client, connections);                    
                exec.execute(connection);
                                   
            }
            catch (Exception e){
                System.out.println(e);
                
            }
            
        }
    }

}
