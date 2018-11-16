window.onload = calendar();
function calendar() {

    var d = new Date();
    var month_name = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'];
    var month = d.getMonth();   //0-11
    var year = d.getFullYear(); //2014
    var first_date = month_name[month] + " " + 1 + " " + year;
    //September 1 2014
    var tmp = new Date(first_date).toDateString();
    //Mon Sep 01 2014 ...
    var first_day = tmp.substring(0, 3);    //Mon
    var day_name = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    var day_no = day_name.indexOf(first_day);   //1
    var days = new Date(year, month+1, 0).getDate();    //30
    //Tue Sep 30 2014 ...
    var month2 = month+1;

    var calendar = get_calendar(day_no, days, month, year, month2);
    document.getElementById("calendar-month-year").innerHTML = month_name[month]+"/"+year;
    document.getElementById("calendar-dates").appendChild(calendar);

    data(month2);


}
function get_calendar(day_no, days, month, year, month2){
    var table = document.createElement('table');
    table.setAttribute("id", "caltab");
    var tr = document.createElement('tr');
    //row for the day letters
    for(var c=0; c<=6; c++){
        var td = document.createElement('td');
        td.innerHTML = "DSTQQSS"[c];
        tr.appendChild(td);
    }
    table.appendChild(tr);


    //create 2nd row
    tr = document.createElement('tr');
    var c;
    for(c=0; c<=6; c++){
        if(c == day_no){
            break;
        }
        var td = document.createElement('td');
        td.addEventListener("click",function(){
            alert("cell clicked");
        });
        td.innerHTML = "";
        tr.appendChild(td);
    }

    var count = 1;
    for(; c<=6; c++){
        var td = document.createElement('td');
        td.addEventListener("click",function(){
            console.log("cell clicked");
            });
        td.innerHTML = count;
        count++;
        tr.appendChild(tad);
    }
    table.appendChild(tr);

    //rest of the date rows
    for(var r=3; r<=7; r++){
        tr = document.createElement('tr');
        for(var c=0; c<=6; c++){
            if(count > days){
                table.appendChild(tr);
                return table;
            }
            var td = document.createElement('td');
            td.innerHTML = count;
            td.className = 'dias';

            td.addEventListener("click",function(){
                var n_month = month+1;
                var date = document.getElementById("calendar-month-year").innerHTML;
                document.getElementById("notes_form").style.visibility= "visible";
                document.getElementById('id_note_date').value = this.innerHTML+"/"+n_month+"/"+year;
            });
            count++;
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }

    return table;

}
function data(month) {
    var dates = document.getElementsByClassName('listas');
    var i;
    var j;
    var dia;
    var dias = [];
    var mes = [];
    var day;
    var days = document.getElementsByClassName('dias');
    for (i = 0; i < dates.length; i++) {
        j = i % 2;
        if (j === 0) {
            dias.push(dates[i].value);

        } else {
            if (parseInt(dates[i].value) === month){
             mes.push(dates[i].value)
            }
        }
    }
    for (day = 0; day < days.length; day++){
        dia =  days[day].innerHTML;
        if(dias.includes(dia)) {
            days[day].style.background = 'green';
        }
    }
    var proj = document.getElementById("heder").innerText;
    document.getElementById(proj).style.visibility = 'visible';
}
function add_project(){
    var parent = document.getElementById('avisos1');
    var element = document.createElement('div');
    element.setAttribute('class', 'projects');
    parent.appendChild(element)

}
function openForm(element) {
    var id = document.getElementById(element);
    id.style.visibility = "visible";
}

function closeForm(element) {
    var id = document.getElementById(element);
    id.style.visibility = "hidden";
}
function go_project(projeto, up){
    var invisible = document.getElementById('heder').innerText;
    document.getElementById(invisible).style.visibility = 'hidden';
    var strings = (projeto.id);
    document.getElementById('heder').innerText = strings;
    document.getElementById(strings).style.visibility = 'visible';

}
function upload() {
    document.getElementById('doc_form').style.visibility ="visible";
}
function proj(id, txt){

    document.getElementById(id).value = txt;
}