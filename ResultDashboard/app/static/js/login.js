<script>
$(document).ready(function(){
        $(".close").click(function(){
            $("#flashmodel").remove();
        });
        $(".strongMsg").click(function(){
             $('#register').modal({
                show: true,
                backdrop:'static'
             });
             alert(1);
        });
        $('#registerButton').click(function () {
            $.ajax({
                url: '/register',
                data: {
                    user: $('.ruser').val(),
                    password: $('.rpassword').val(),
                    confirm: $('.rconfirm').val(),
                    email: $('.remail').val(),
                },
                type: 'POST',
                success: function (data) {
                    if(data && data.success){
                        windows.location.href = "/index";
                    }else{
                        if(data.errors.hasOwnProperty("user")){
                            $(".ruser").val("");
                            $(".ruser").attr("placeholder",data.errors.user[0]);
                        }else if(data.errors.hasOwnProperty("password")){
                            $(".rpassword").val("");
                            $(".rpassword").attr("placeholder",data.errors.password[0]);
                        }else if(data.errors.hasOwnProperty("confirm")){
                            $(".confirm").val("");
                            $(".rpassword").attr("placeholder",data.errors.confirm[0]);
                        }else if(data.errors.hasOwnProperty("email")){
                            $(".remail").val("");
                            $(".remail").attr("placeholder",data.errors.email[0]);
                        }
                    }

                },
                error: function (data) {

                }
            });
        });
});
</script>