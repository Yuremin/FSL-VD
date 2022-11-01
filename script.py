import os
import re





def find_files_in_dir(directory, regex, silent=True):
	matching_files = []
	for root, dirs, files in os.walk(directory):
		for name in files:
			result = re.search(regex, name, re.IGNORECASE)
			if result != None:
				matching_files.append(os.path.realpath(os.path.join(root, name)))
			else:
				if not silent:
					print("Skipped file (did not match regex): ", name)

	return matching_files


def extract_cwe_id_from_path(path):
    cwe_id_regex = "(CWE\d+)_"
    cwe_id = ""
    if os.path.basename(path).startswith('CWE'):
        cwe_id = re.search(cwe_id_regex, os.path.basename(path)).group(1)
    else:
        cwe_id = re.search(cwe_id_regex, path).group(1)
        sub_dir = os.path.basename(path)
        cwe_id = cwe_id + "_" + sub_dir
    return cwe_id


if __name__=="__main__":
    extract_cwe_id_from_path("data")
