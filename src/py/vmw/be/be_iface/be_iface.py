class BEInterface(object):
    """ This class offers method to interface the Frontend/UI to the Backend """

    def __init__(self):
        print('Class BackendInterface created')

    def get_file_headers(self, file_id):
        """
        Gets the headers read from the file represented by the file_id
        Arguments:
            file_id: filename string
        Returns:
            List of headers found in the either the csv or the vcf file.
        Raises:
            Exception
        """
        print('get_file_headers called...File id: {0}'.format(file_id))
        return []

    def get_sample_ids(self):
        """
        Gets the file names of each file to be merged by extracting it from the absolute path.
        Returns:
            List of file names
        """
        print('get_sample_ids called')
        return []

    def get_common_headers(self):
        """
        Gets the headers which are common to all files.
        Returns:
            List of common headers
        Raises:
            Exception
        """
        print('get_common_headers called')
        return []

    def get_merge_progress(self):
        """
        Returns the progress of the merge process, returning a percentage of the current progress.
        Returns:
            Integer representing a percentage.
        Raises:
            Exception
        """
        print('get_merge_progress called')
        return 0

    def merge(self):
        """
        This method starts the merge process in the backend.
        """
        print('merge called')

    def set_output_filename(self, output_filename='output.csv'):
        """
        Set output file name.
        Arguments:
            output_filename: the file name to be used for the final result. Default file name is 'output.csv'
        """
        print('set_output_filename called...file name: {0}'.format(output_filename))

    def set_merge_columns(self, join_columns_list):
        """
        Set which columns are going to be used to join all files.
        Arguments:
            join_columns_list: a list of headers on which to join all files.
        """
        print('set_merge_column_fields called...columns: {0}'.format(join_columns_list))

    def set_common_output_columns(self, columns_list):
        """
        Set those columns which should appear in the output file, given they are common in all files.
        Arguments:
            columns_list: a list of headers which are common in all files to merge.
        """
        print('set_output_columns called...columns: {0}'.format(columns_list))

    def set_additional_output_columns(self, file_columns_tuple_list):
        """
        Set additional columns which are not common to all files.
        Arguments:
            file_columns_tuple_list: a list of tuples containing the file_id and corresponding additional fields
        """
        print('set_additional_output_columns: {0}'.format(file_columns_tuple_list))

    def set_files_to_merge(self, file_list):
        """
        Set the files which are going to be merged. This applies to csv or vcf only files. 
        Arguments:
            file_list: a list of files in absolute path format
        Raises:
            Exception
        """
        print('set_files_to_merge called...files: {0}'.format(file_tuple_list))

    def set_paired_files_to_merge(self, file_tuple_list):
        """
        Set the files which are going to be merged as a pair. This applies when merging csv to vcf files.
        Arguments:
            file_tuple_list: a list of tuples containing the vcf paired to its equivalent csv annot file
        Raises:
            Exception
        """
        print('set__paired_files_to_merge called...files: {0}'.format(file_tuple_list))
