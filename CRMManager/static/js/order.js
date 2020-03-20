


  $("#id_date_finish").change(function () {
      var serializedData = $(this).serialize();
      var myform = document.getElementById("myform");
      var fd = new FormData(myform);
       $.ajax({
        url : "{% url 'post_order' %}", // the endpoint
        type : "POST", // http method
        data : { date : $('#id_date_finish').val() , // data sent with the post request
                 id: '{{order.id}}',
                 csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        serializedData,},


        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {

        }
    });


  })

    /*
        On submiting the form, send the POST ajax
        request to server and after successfull submission
        display the object.
    */
    $("#customer-form").submit(function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "{% url 'post_customer' %}",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // 1. clear the form.
                $("#customer-form").trigger('reset');
                // 2. focus to nickname input
                $("#id_name").focus();

                // display the newly friend to table.
                var instance = JSON.parse(response["instance"]);
                var fields = instance[0]["fields"];
                $("#my_customers tbody").prepend(
                    `<tr>
                    <td>${fields["name"]||""}</td>
                    <td>${fields["company"]||""}</td>
                    <td>${fields["phone"]||""}</td>
                    <td>${fields["email"]||""}</td>
                    <td>${fields["address"]||""}</td>
                    </tr>`
                )
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })




    $("#task-form").submit(function (e) {
        // preventing from page reload and default actions

        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();

        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "{% url 'post_task' order.id %}",
            data: serializedData,
            success: function (response) {

                // on successfull creating object
                // 1. clear the form.
                $("#task-form").trigger('reset');
                // 2. focus to nickname input
                $("#task").focus();

                // display the newly friend to table.
                var instance = JSON.parse(response["instance"]);
                var fields = instance[0]["fields"];
                $("#my_tasks tbody").prepend(
                    `<tr>
                    <td >${fields["task"]||""}</td>
                    </tr>`
                )
            },
            error: function (response) {

                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })


     $("#service-form").submit(function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "{% url 'post_service' order.id %}",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // 1. clear the form.
                $("#service-form").trigger('reset');
                // 2. focus to nickname input
                $("#id_name").focus();

                // display the newly friend to table.
                var instance = JSON.parse(response["instance"]);
                var fields = instance[0]["fields"];
                $("#my_services tbody").append(
                    `<tr>
                    <td contenteditable="true">${fields["service"]||""}</td>
                    <td contenteditable="true">${fields["quantity"]||""}</td>
                    <td contenteditable="true">${fields["price"]||""} ₪</td>
                     <td><input type="submit" class="btn btn-danger justify-content-center text-center" value="מחק"  /></td>
                    </tr>`
                )
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })


      $("#file-form").submit(function (e) {
        var data = new FormData($('#file-form').get(0));
        data.append('id_file',$("#id_file").files[0]);
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "{% url 'post_file' order.id %}",
            data: {'data' : data},
            success: function (response) {
                // on successfull creating object
                // 1. clear the form.
                $("#file-form").trigger('reset');
                // 2. focus to nickname input
                // splay the newly friend to table.
                var instance = JSON.parse(response["instance"]);
                var fields = instance[0]["fields"];

            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })


    /*
    On focus out on input nickname,
    call AJAX get request to check if the nickName
    already exists or not.
    */
     /*
    $("#id_name").focusout(function (e) {
        e.preventDefault();
        // get the nickname
        var name = $(this).val();
        // GET AJAX request
        $.ajax({
            type: 'GET',
            url: "{% url 'validate_name' %}",
            data: {"name": name},
            success: function (response) {
                // if not valid user, alert the user
                if(!response["valid"]){
                    alert("You cannot create a friend with same nick name");
                    var Name = $("#id_name");
                    Name.val("")
                    Name.focus()
                }
            },
            error: function (response) {
                console.log(response)
            }
        })
    })

      */


