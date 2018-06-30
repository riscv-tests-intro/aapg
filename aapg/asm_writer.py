"""
    asm_writer Class for writing assembly code to file
"""
import logging

def indent_string(content, indent):
    """ Utility function to indent a string by given levels """
    return ''.join(['\t']*indent) + content

class AsmWriter(object):
    """ Class that creates methods for writing various sections to file
        
        Params:
            ofile: Output file handler
    """

    def __init__(self, ofile):
        """ Instantiate a class for writing to a file
        Args:
            ofile: Output file handler
            
        Return:
            writer: AsmWriter class
        """
        self.ofile = ofile

    def comment(self, comment, indent=0, comment_init = '#'):
        """ Function that writes a GAS comment to the ofile

            Args:
                comment: (str) Comment
                indent: (int) Indentation level
                comment_init: (str) Comment symbol

            Returns:
                None
        """
        ofile = self.ofile
        write_string = indent_string('# ' + comment, indent) + '\n'
        ofile.write(write_string)

    def newline(self, count = 1):
        """ Inserts (count) newlines """
        self.ofile.write(''.join(['\n']*count))

    def write(self, content, comment = None, indent = 1):
        """ Write arbitrary content to file

            Args:
                content: (str) Content to write
                comment: (str) Inline comment to add
                indent: (int) Indentation level

            Returns:
                None
        """
        ofile = self.ofile
        write_string = indent_string(content, indent)
        write_string = write_string + ('\t\t' + '# ' + comment + '\n' if comment is not None else '')
        write_string += '\n'
        ofile.write(write_string)

    def write_inst(self, inst_name, *args, **kwargs):
        """ Write an instruction to the file

            Args:
                inst_name: (str) Name of 
                args: ([str]) List of arguments to function
                comment: (str) Comment to add
                indent: (int) Tabs to indent
            
            Returns:
                None
        """
        ofile = self.ofile
        if kwargs is not None:
            indent = kwargs['indent'] if 'indent' in kwargs else 1
            comment = '# ' + kwargs['comment'] if 'comment' in kwargs else ''

        write_string = '{0:<20s}{1:<20s}{2}\n'.format(inst_name, ', '.join(args), comment)
        write_string = indent_string(write_string, indent)
        ofile.write(write_string)
