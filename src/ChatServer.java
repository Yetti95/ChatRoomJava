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
    private static boolean on = true;
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
