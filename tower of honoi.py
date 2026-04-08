def tower_of_honoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_honoi(n-1, source, destination, auxiliary)
    print("move disk", n, "from", source, "to", destination)
    tower_of_honoi(n-1, auxiliary, source, destination)

n = int(input("enter number of disk:"))
tower_of_honoi(n, 'A', 'B', 'C')
