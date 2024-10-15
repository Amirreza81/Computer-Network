# Computer Network - Sharif University of Technology2

Theoretical and practical assignments and project of CN at Sharif Univercity of Technology (CE-443)<br _>

Brief explanation of practical assignments with their solutions:

* ## HW1 - Telnet, DNS, HTTP, Netstat

* ## HW2 - Load Balancer

    This project simulates a simple **Load Balancer** that distributes incoming traffic among multiple backend servers using a **Round Robin** algorithm. The goal is to improve scalability and enhance the responsiveness of the web applications behind the load balancer.

    ### Features
    1. **Round Robin Load Balancing**: The load balancer distributes incoming requests sequentially to the available backend servers.
    2. **Health Check**: Periodically checks the health of the backend servers by sending a test request.
    3. **Connection Handling**: Establishes a connection with a backend server, forwards the client request, and returns the response to the client.
    4. **Configuration File**: The backend servers and their corresponding ports are configured through a file.

    ### Project Structure

    - **server.py**: Implements a simple backend server that listens to incoming requests and returns a response indicating its instance number.
    - **service.py**: Contains logic for server-side operations and health checks.
    - **hw2.py**: Main script that runs the load balancer and manages the distribution of client requests across servers.

    ## How to Run

    1. **Configure Backend Servers**: Create a configuration file `config.txt` in the following format:
        ```
        [ip0] [port0]
        [ip1] [port1]
        [ip2] [port2]
        ```
        Example:
        ```
        127.0.0.1 8000
        127.0.0.1 8001
        127.0.0.1 8002
        ```

    2. **Start Backend Servers**: Run each backend server using the `server.py` file. You can do this by opening multiple terminal windows:
        ```bash
        python server.py 8000
        python server.py 8001
        python server.py 8002
        ```

    3. **Run the Load Balancer**: Once the backend servers are running, you can start the load balancer:
        ```bash
        python hw2.py config.txt
        ```

    4. **Test the Load Balancer**: The load balancer will forward client requests to different backend servers in a round-robin fashion and handle server health checks.

    ### Example Output

    Each backend server returns its instance number:
        ```
        It's instance number 1
        It's instance number 2
        It's instance number 3
        ```

    Logs from the load balancer will indicate which server handled each request and the health check status.

    ### Evaluation Criteria

    The load balancer will be tested by sending a large number of requests. The distribution of requests should be almost equal across all backend servers, demonstrating the proper functionality of the round-robin algorithm.

* ## HW3 - Routing Simulation
