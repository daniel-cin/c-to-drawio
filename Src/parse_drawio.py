import tools
from N2G import drawio_diagram
import string 


class c_code_2_mermaid:

    def __init__(self, text_file_path, output_path) -> None:
        self.diagram = drawio_diagram()
        self.text_file_path = text_file_path
        self.output_path = output_path
        self.raw_text_list = []
        self.final_text_list = []
        self.md_output_string = ""
        self.do_pipeline()

    def do_pipeline(self):
        self.open_text_file()
        self.pre_process_text()
        self.write_drawio_file()

    def open_text_file(self):
        with open(self.text_file_path, 'r',  encoding='utf-8') as file:
            content = file.readlines()
            content = [line.strip() for line in content]
            self.raw_text_list = content
            print(content)

    def pre_process_text(self):
        for index, line in enumerate(self.raw_text_list):
            # print(f"{index}) {line=}")
            line = line.replace("{", "").replace("}", "")
            line = line.replace("}", "").replace("}", "")
            if line:
                self.final_text_list.append(line)
            # print(f"{index}) {line=}")
        tools.print_text_list(self.final_text_list)

    def create_drawio_block(self, line_code, line_id):
        print("create_drawio_block:\t ",line_code)
        txt=line_code.replace("<", "&lt;").replace("&", "&amp;").replace(">", "&gt;").replace('\"', "&#34;")
        print(txt)
        y_pos = line_id *100
        self.diagram.add_node(id=tools.number_to_letter(line_id) ,label=txt, y_pos=y_pos)

    def write_drawio_file(self):
        self.diagram.add_diagram("CFG")
        for index, line in enumerate(self.final_text_list):
            print(f'{index=} ; \t {line=}')
            self.create_drawio_block(line, index)
        self.diagram.dump_file(filename="CFG.drawio", folder=self.output_path)
 


if __name__ == "__main__":
    C_FILE = r"Examples/main.c"
    DIR_OUTPUT = r"Output"
    teste = c_code_2_mermaid(text_file_path=C_FILE, output_path=DIR_OUTPUT)
