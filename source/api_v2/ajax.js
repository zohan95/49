

$.ajax({

    url: 'http://localhost:8000/api/v2/login/',

    method: 'post',

    data: JSON.stringify({username: 'admin', password: 'admin'}),

    dataType: 'json',

    contentType: 'application/json',

    success: function(response, status){processes()},

    error: function(response, status){console.log(response);}

});






function processes(){

$.ajax({

     url: 'http://127.0.0.1:8000/api/v2/projectss/',

     method: 'get',

     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},

     dataType: 'json',

     contentType: 'application/json',

     success: function(response, status){console.log(response);},

     error: function(response, status){console.log(response);}

});


$.ajax({

     url: 'http://127.0.0.1:8000/api/v2/taskss/',

     method: 'get',

     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},

     dataType: 'json',

     contentType: 'application/json',

     success: function(response, status){console.log(response);},

     error: function(response, status){console.log(response);}

});



$.ajax({

     url: 'http://127.0.0.1:8000/api/v2/projectss/<pk of project>/',

     method: 'get',

     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},

     dataType: 'json',

     contentType: 'application/json',

     success: function(response, status){console.log(response['projectz'])},

     error: function(response, status){console.log(response);}

});


$.ajax({

     url: 'http://127.0.0.1:8000/api/v2/taskss/',

     method: 'post',

     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},

     data: JSON.stringify({summary:'sdsd', description:'sdasdcs', task_status:'2',task_type:'2',project:'1'}),

     dataType: 'json',

     contentType: 'application/json',

     success: function(response, status){console.log(response);},

     error: function(response, status){console.log(response);}

});


$.ajax({

     url: 'http://127.0.0.1:8000/api/v2/taskss/<pk of task>/',

     method: 'delete',

     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},



     dataType: 'json',

     contentType: 'application/json',

     success: function(response, status){console.log(response);},

     error: function(response, status){console.log(response);}

});}
