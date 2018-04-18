import java.util.*;
import java.net.*;

public class BroadcastThread implements Runnable 
{ 
	private List<Map<String, Socket>> connections;
	private String lastMessage;
	public BroadcastThread(List<Map<String, Socket>> connections) {
		this.connections = connections;
	}
    public void run() { 
        while (true) { 
            // sleep for 1/10th of a second 
            try { Thread.sleep(100); } catch (InterruptedException ignore) { }
            /** 
             * check if there are any messages in the Vector. If so, remove them 
             * and broadcast the messages to the chatroom 
             */ 
        } 
    } 
}
