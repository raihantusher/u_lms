$(document).ready(function(){


    $('#loginUser').submit(function(e){
        e.preventDefault();
        var username = $('.username').val();
        var password = $('.password').val();
        if(username == '' || password == ''){
            $('#userLogin_form .modal-body').append('<div class="alert alert-danger">Please Fill All The Fields.</div>');
        }else{
            $.ajax({
                url: 'php_files/user.php',
                method: 'POST',
                data: {login:'1',username:username,password:password},
                dataType: 'json',
                success: function(response){
                    $('.alert').hide();
                    console.log(response);
                    var res = response;
                    if(res.hasOwnProperty('success')){
                        $('#userLogin_form .modal-body').append('<div class="alert alert-success">LoggedIn Successfully.</div>');
                        setTimeout(function(){ location.reload(); }, 1000);
                    }else if(res.hasOwnProperty('error')){
                        $('#userLogin_form .modal-body').append('<div class="alert alert-danger">'+res.error+'</div>');
                    }

                }
            });
        }
    });



  
    $('.user_logout').click(function(e){
        e.preventDefault();
        var user_logout = 1;
        $.ajax({
            url: 'php_files/user.php',
            method: 'POST',
            data: {user_logout:user_logout},
            success: function(response){
                if(response == 'true'){
                    location.reload();
                }
            }
        });
    });

    
    $('#register_sign_up').submit(function(e){
        e.preventDefault();
        $('.alert').hide();
        var f_name = $(".first_name").val();
        var l_name = $(".last_name").val();
        var username = $(".user_name").val();
        var email = $(".e_mail").val();
        var password = $(".pass_word").val();
        var mobile = $(".mobile").val();
        var address = $(".address").val();
        var city = $(".city").val();

        if (f_name == '' || l_name == '' || username == '' ||  email == '' || password == '' || mobile == '' || address == '' || city == ''){
            $('#register_sign_up').append('<div class="alert alert-danger">Please Fill All The Fields</div>');
        }else{
            var formdata = new FormData(this);
            formdata.append('create','1');
            $.ajax({
            url:"php_files/user.php",
            type:"POST",
            data: formdata,
            contentType: false,
            processData: false,
            dataType: 'json',
            success:function(response){
                $('.alert').hide();
                var res = response;
                if(res.hasOwnProperty('success')){
                    $('#register_sign_up').append('<div class="alert alert-success">'+res.success+'</div>');
                    setTimeout(function(){ window.location.href = 'user_profile.php'; }, 1500);
                }else if(res.hasOwnProperty('error')){
                    $('#register_sign_up').append('<div class="alert alert-danger">'+res.error+'</div>');
                }
            }
        });
        }
    });

    $('#modify-user').submit(function(e){
        e.preventDefault();
        var f_name = $(".first_name").val();
        var l_name = $(".last_name").val();
        var email = $(".e_name").val();
        var mobile = $(".mobile").val();
        var address = $(".address").val();
        var city = $(".city").val();

        if (f_name == '' || l_name == '' ||  email == '' || mobile == '' || address == '' || city == ''){
            $('#modify-user').append('<div class="alert alert-danger">Please Fill All The Fields</div>');
        }else{
            var formdata = new FormData(this);
            formdata.append('update','1');
            $.ajax({
                url:"php_files/user.php",
                type:"POST",
                data: formdata,
                contentType: false,
                processData: false,
                dataType: 'json',
                success:function(response){
                    $('.alert').hide();
                    var res = response;
                    if(res.hasOwnProperty('success')){
                        $('#modify-user').append('<div class="alert alert-success">Modified Successfully.</div>');
                        setTimeout(function(){ window.location.href = 'user_profile.php'; }, 1500);
                    }else if(res.hasOwnProperty('error')){
                        $('#modify-user').append('<div class="alert alert-danger">'+res.error+'</div>');
                    }
                    
                }
            });
        }
    });


    $('#modify-password').submit(function(e){
        e.preventDefault();
        $('.alert').hide();
        var old_pass = $(".old_pass").val();
        var new_pass = $(".new_pass").val();

        if (old_pass == '' || new_pass == ''){
            $('#modify-password').append('<div class="alert alert-danger">Please Fill All The Fields</div>');
        }else{
            var formdata = new FormData(this);
            formdata.append('modifyPass','1');
            $.ajax({
                url:"php_files/user.php",
                type:"POST",
                data: formdata,
                contentType: false,
                processData: false,
                dataType: 'json',
                success:function(response){
                    $('.alert').hide();
                    var res = response;
                    if(res.hasOwnProperty('success')){
                        $('#modify-password').append('<div class="alert alert-success">Password Modified Successfully.</div>');
                        setTimeout(function(){ window.location.href = 'user_profile.php'; }, 1500);
                    }else if(res.hasOwnProperty('error')){
                        $('#modify-password').append('<div class="alert alert-danger">'+res.error+'</div>');
                    }
                    
                }
            });
        }
    });

 
//delete_download_book
    $('.delete_download_book').click(function(){
        var tr = $(this);
        var id = $(this).attr('data-id');
        if(confirm('Are you Sure want to delete this')){
            $.ajax({
                url: '/my_downloads.php',
                type: 'POST',
                data: {delete_id:id},
                dataType: 'json',
                success: function(response){
                    var res = response;
                    if(res.hasOwnProperty('success')){
                        tr.parent().parent('tr').remove();
                    }
                }
            });
        }
    });

 
   


});