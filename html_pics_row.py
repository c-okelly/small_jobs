# Generate a 3 wide html row of pics from a given directory all filled in
# Could make this flexible in the future

template_code = '<!-- Projects Row --> \
        <div class="row"> \
            <div class="col-md-4 portfolio-item"> \
                <img class="img-responsive" src="'+loc_1+'" alt="">\
            </div> \
            <div class="col-md-4 portfolio-item"> \
                <img class="img-responsive" src="'+loc_2+'" alt=""> \
            </div> \
            <div class="col-md-4 portfolio-item"> \
                <img class="img-responsive" src="'+loc_3+'" alt=""> \
            </div> \
        </div> \
        <br><br> \
        <!-- /.row -->'