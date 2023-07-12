import sys

# Initialize variables
total_file_size = 0
status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Parse the line
        parts = line.split(' ')
        file_size = int(parts[-1])
        status_code = parts[-2]
        
        # Update metrics
        total_file_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1
        
        line_count += 1
        
        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            
            # Print number of lines by status code in ascending order
            for status_code in sorted(status_counts.keys()):
                count = status_counts[status_code]
                if count > 0:
                    print(f"{status_code}: {count}")
        
except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print("\nProgram interrupted.")

# Print final statistics
print(f"\nTotal file size: {total_file_size}")

# Print number of lines by status code in ascending order
for status_code in sorted(status_counts.keys()):
    count = status_counts[status_code]
    if count > 0:
        print(f"{status_code}: {count}")

