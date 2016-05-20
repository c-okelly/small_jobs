# Generate a 3 wide html row of pics from a given directory all filled in
# Could make this flexible in the future

import os

def main(search_directory,link_directory):

    # Find all files in directory and run them through clean_html_and_save_to_file
    all_files = os.listdir(search_directory)
    # Non hidden files
    non_hidden = [file_name for file_name in all_files if file_name[0] != "."]
    # print(non_hidden)


    ## Cycle through list and genreate html text
    list_index_range = len(non_hidden) -1
    for i in range(0,len(non_hidden),3):
        loc_1 = link_directory + non_hidden[i]
        if i+1 > list_index_range:
            loc_2 = "out of range"
        else:
            loc_2 = link_directory + non_hidden[i+1]
        if i+2 > list_index_range:
            loc_3 = "out of range"
        else:
            loc_3 = link_directory + non_hidden[i+2]

        template_code = '<!-- Projects Row --> \n\
                <div class="row"> \n\
                    <div class="col-md-4 portfolio-item"> \n\
                        <img class="img-responsive" src="'+loc_1+'" alt="">\n\
                    </div> \n\
                    <div class="col-md-4 portfolio-item"> \n\
                        <img class="img-responsive" src="'+loc_2+'" alt=""> \n\
                    </div> \n\
                    <div class="col-md-4 portfolio-item"> \n\
                        <img class="img-responsive" src="'+loc_3+'" alt=""> \n\
                    </div> \n\
                </div> \n\
                <br><br> \n\
                <!-- /.row -->'
    print(template_code)


if __name__ == '__main__':
    print("hi")
    main("/Users/cokelly/Google_Drive/Teir 2/Website building/briankellycsi.ie/Most recent/briankellycsi.ie/images/restoration_page/g_volvo/0_taken_apart","images/restoration_page/g_volvo/0_taken_apart/")