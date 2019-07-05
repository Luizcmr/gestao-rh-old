$("#id_empresa").change(function () {
  var url = $("#contratoForm").attr("data-funcionarios-url");  // get the url of the `load_cities` view
  var empresaId = $(this).val();  // get the selected country ID from the HTML input

  $.ajax({                       // initialize an AJAX request
    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
    data: {
      'empresa': empresaId       // add the country id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the `load_cities` view function
      $("#id_funcionario").html(data);  // replace the contents of the city input with the data that came from the server
    }
  });

});

// Script para scrol nas tabelas
$(document).ready(function () {
  $('#dtHorizontalVerticalExample').DataTable({
    "order": [[ 3, "desc" ]],
    "pagingType": "simple_numbers",
    "scrollX": true,
    "scrollY": 200,
  });
  $('.dataTables_length').addClass('bs-select');
});

function calculaDataFin() {
var datainicial = document.getElementById("dataini").value;
var dias = parseInt(document.getElementById("dias").value);
var partes = datainicial.split("/");
var dia = partes[0];
var mes = partes[1]-1;
var ano = partes[2];

datainicial = new Date(ano,mes,dia);
datafinal = new Date(datainicial);
datafinal.setDate(datafinal.getDate() + dias);

var dd = ("0" + datafinal.getDate()).slice(-2);
var mm = ("0" + (datafinal.getMonth()+1)).slice(-2);
var y = datafinal.getFullYear();

var dataformatada = dd + '/' + mm + '/' + y;
document.getElementById('datafin').value = dataformatada;

}

