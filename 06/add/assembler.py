JUMP = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

DEST = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

COMP = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "X": "110000",
    "!D": "001101",
    "!X": "110001",
    "-D": "001111",
    "-X": "110011",
    "D+1": "011111",
    "X+1": "110111",
    "D-1": "001110",
    "X-1": "110010",
    "D+X": "000010",
    "D-X": "010011",
    "X-D": "000111",
    "D&X": "000000",
    "D|X": "010101"
}

def clean_code(file):
    lines = []
    for line in file:
        if "//" in line[0:2] or line == "\n":
            continue
        if "//" in line:
            index = line.find("/")
            line = line[:index]
        line = line.strip().replace(" ", "") # strip removes trailing spaces and replace removes in-between spaces.
        lines.append(line)

    return lines

def parse_C(line):
    # Separators => "=", ";" (I don't line below code)
    dest, jmp = "", ""
    comp = line
    if "=" in line:
        dest = line.split("=")[0]
        comp = line.split("=")[1]
    # from here on, line is without "="
    if ";" in line:
        jmp = comp.split(";")[1]
        comp = comp.split(";")[0]
    return [dest, comp, jmp]

def parser(instruction_list):
    # Separate line into different fields.
    fields = []
    for item in instruction_list:
        if item[0] == "@":
            fields.append(list(item)) # '@3' becomes ['@', '3']
        else:
            fields.append(parse_C(item));
    return fields

def string_to_binary(string):
    bin = format(int(string), "b")
    zero_count = 15 - len(bin)
    bin = "0" * zero_count + bin
    return bin

def comp_bits(string):
    if "M" in string:
        return "1" + COMP[string.replace("M", "X")]
    if "A" in string:
        string = string.replace("A", "X")

    return "0" + COMP[string]
        

def decode(fields):
    # NOTE - Before coming here, Symbol thingy has already happened!
    # Decode and organize into binary instructions
    # for each field, A-instruction = ["@", value], C-instruction = [dest, comp, jmp]
    binary = []
    for item in fields:
        if item[0] == "@":
            # convert address into binary with preceeding 0's to complete 15
            binary.append("0" + string_to_binary(item[1]))
        else:
            dest = DEST[item[0]]

            binary.append("111" + comp_bits(item[1]) + DEST[item[0]] + JUMP[item[2]])
    return binary

def main():
    with open("Add.asm", "r") as file:
        instruction_list = clean_code(file)
        fields = parser(instruction_list)

        # Symbols have to be introduced after this line
        binary = decode(fields)
    
    with open("Add.hack", "w") as file:
        for line in binary:
            file.write(line + "\n")

if __name__ == "__main__":
    main()