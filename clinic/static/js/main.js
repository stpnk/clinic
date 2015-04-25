

var year = $('#id_date_year').val(),
    time = $('#id_time').val()


$('#id_doctor, #id_date_month, #id_date_day, #id_date_year').change(function(){

    $('#weekend').text('')
    $('#id_time').find('option:disabled').removeAttr('disabled');

    if ($('#id_doctor').val() != '') {
        
        doctor = $('#id_doctor').val();
        date = $('#id_date_month').val() + '-' + $('#id_date_day').val() + '-' + $('#id_date_year').val();
    
        $.ajax({
            url:'get-schedule/' + doctor + '/' + date + '/'
        })
        .done(function(data){
            if (data.weekday === 5){
                $('#weekend').text('Выходной день!')
                $('#id_time').find('option').attr('disabled', 'disabled');   
            } else if (data.weekday === 6){
                $('#weekend').text('Выходной день!')
                $('#id_time').find('option').attr('disabled', 'disabled');
            }
            arr = data.schedule_time
            arr.forEach(function(item,i,arr){
                $('#id_time option[value="' + item + '"]').attr('disabled', 'disabled');
            });
        
        });
    }
});