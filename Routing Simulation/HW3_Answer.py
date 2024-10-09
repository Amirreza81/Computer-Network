import ipaddress

id_of_links = []
sorted_ids = []
ip_of_links = {}
sorted_ips = {}
distance_of_links = {}
neighbours_distance = {}


def route(command):
    main_and_neighbour_distance = {}
    roots = {}
    sorted_roots = {}
    main_and_neighbour_ips = []
    for id in id_of_links:
        main_and_neighbour_ips.append(ip_of_links[id])
        if ip_of_links[id] not in main_and_neighbour_distance.keys():
            main_and_neighbour_distance[ip_of_links[id]] = distance_of_links[id]
        elif main_and_neighbour_distance[ip_of_links[id]] > distance_of_links[id]:
            main_and_neighbour_distance[ip_of_links[id]] = distance_of_links[id]

        roots[ip_of_links[id]] = id

        for ip in neighbours_distance[id].keys():
            temp_dist = distance_of_links[id] + (neighbours_distance[id])[ip]
            if ip not in main_and_neighbour_distance.keys():
                main_and_neighbour_distance[ip] = temp_dist
            elif main_and_neighbour_distance[ip] > temp_dist:
                main_and_neighbour_distance[ip] = temp_dist

            main_and_neighbour_ips.append(ip)
            roots[ip] = id

    main_and_neighbour_ips = list(set(main_and_neighbour_ips))
    routing(command, main_and_neighbour_ips, roots)


def routing(command, main_and_neighbour_ips, roots):
    original_ip = command[1]
    main_and_neighbour_ips.sort()
    counter = 0
    for ip in main_and_neighbour_ips:
        if ipaddress.ip_address(original_ip) in ipaddress.ip_network(ip):
            counter += 1
            print(roots[ip])
        else:
            continue
    if counter == 0:
        print("No route found")


def add_link(command):
    id = command[2]
    neighbours_distance[id] = {}
    id_of_links.append(id)
    ip = command[3]
    ip_of_links[id] = ip
    dist = int(command[4])
    distance_of_links[id] = dist
    sorted_ids = id_of_links.sort()


def remove_link(command):
    neighbours_distance.pop(command[2])
    id = command[2]
    id_of_links.remove(id)
    ip_of_links.pop(id)
    distance_of_links.pop(id)


def print_links():
    global ip_of_links
    main_and_neighbour_ips = []
    ip_of_links = {k: v for k, v in sorted(ip_of_links.items(), key=lambda item: item[1])}
    sorted_ips = ip_of_links
    main_and_neighbour_distance = {}

    for id in id_of_links:
        if ip_of_links[id] not in main_and_neighbour_distance.keys():
            main_and_neighbour_distance[ip_of_links[id]] = distance_of_links[id]
        else:
            main_dist = min(main_and_neighbour_distance[ip_of_links[id]], distance_of_links[id])
            main_and_neighbour_distance[ip_of_links[id]] = main_dist

        for dist in neighbours_distance[id].keys():
            if dist not in main_and_neighbour_distance.keys():
                main_dist = distance_of_links[id] + (neighbours_distance[id])[dist]
                main_and_neighbour_distance[dist] = main_dist
            else:
                second_dist = distance_of_links[id] + (neighbours_distance[id])[dist]
                main_dist = min(main_and_neighbour_distance[dist], second_dist)
                main_and_neighbour_distance[dist] = main_dist
            main_and_neighbour_ips.append(dist)
        main_and_neighbour_ips.append(ip_of_links[id])

    main_and_neighbour_ips = list(set(main_and_neighbour_ips))
    printing(main_and_neighbour_ips, main_and_neighbour_distance)


def printing(main_and_neighbour_ips, main_and_neighbour_distance):
    main_and_neighbour_ips.sort()
    for ip in main_and_neighbour_ips:
        dist_of_lnk = main_and_neighbour_distance[ip]
        print(ip, dist_of_lnk)


def update_link(command):
    id = command[1]
    counter = int(command[2])
    for count in range(counter):
        inp = input().split()
        ip = inp[0]
        dist = int(inp[1])
        (neighbours_distance[id])[ip] = dist


def main():
    command = input().split()
    inp = command[0]
    while inp != 'exit':
        if inp == 'add':
            add_link(command)
        elif inp == 'remove':
            remove_link(command)
        elif inp == 'update':
            update_link(command)
        elif inp == 'print':
            print_links()
        elif inp == 'route':
            route(command)
        command = input().split()
        inp = command[0]


if __name__ == '__main__':
    main()
