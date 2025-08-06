def remove_834_blocks(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    output_lines = []
    in_block = False
    block_lines = []
    block_has_target_INS = False
    removed_blocks_count = 0

    # Add all patterns to be removed here:
    target_INS_patterns = [
        'INS*Y*18*001*AI*C*E*1',
        'INS*Y*19*001*AI*C*E*1',
        'INS*N*01*001*AI*C*E*1'
    ]

    for line in lines:
        line = line.strip()
        if line.startswith('ST*'):
            in_block = True
            block_lines = [line]
            block_has_target_INS = False
        elif line.startswith('SE*') and in_block:
            block_lines.append(line)
            if not block_has_target_INS:
                output_lines.extend(block_lines)
            else:
                removed_blocks_count += 1
            in_block = False
            block_lines = []
        elif in_block:
            block_lines.append(line)
            if any(line.startswith(pattern) for pattern in target_INS_patterns):
                block_has_target_INS = True
        else:
            output_lines.append(line)

    with open(output_file, 'w') as outfile:
        for line in output_lines:
            outfile.write(line + '\n')

    print(f"Done! Cleaned file saved as {output_file}")
    print(f"Total blocks removed: {removed_blocks_count}")

if __name__ == "__main__":
    input_filename = input("Enter the input file name (with extension): ")
    output_filename = input("Enter the desired output file name: ")
    remove_834_blocks(input_filename, output_filename)
