var destination = null;

function my_showAddAnotherPopup(obj, jqobj){
    destination = jqobj.parent().find("input:text");
    console.log(destination);
    return showAddAnotherPopup(obj);
};

function append_addNew_button(name, selector){
    var addNew_html = '<a href="/admin/acquisti/' + name + '/add"';
    
    if (name=='prodotto' || name=='unita_misura'){
        var my_id = $(selector).parent().attr("id").replace("righe_fattura_acquisto-", "");
        my_id='id_' + name + '_' + my_id
    }else{
        var my_id = 'id_' + name
    }
    
    addNew_html += ' id="' + my_id + '"';
    addNew_html += ' class="add-another" onclick="return my_showAddAnotherPopup(this, $(this));">';
    addNew_html += '<img src="/static/admin/img/icon_addlink.gif" width="10" height="10" alt="Aggiungi un altro ' + name + '"/>';
    addNew_html += '</a>';
    
    $(selector).append(addNew_html);
};

dismissAddAnotherPopup = function(win, newId, newRepr){
    // newId and newRepr are expected to have previously been escaped by
    // django.utils.html.escape.
    newId = html_unescape(newId);
    newRepr = html_unescape(newRepr);
    var name = windowname_to_id(win.name);
    
    if (name.indexOf("id_prodotto_") == 0){
      name = name.replace("id_prodotto_", "");
      name = "id_righe_fattura_acquisto-" + name + "-prodotto";
    };

    if (name.indexOf("id_unita_misura") == 0){
      name = name.replace("id_unita_misura_", "");
      name = "id_righe_fattura_acquisto-" + name + "-unita_di_misura";
    };

    var elem = document.getElementById(name);
    if (elem) {
        var elemName = elem.nodeName.toUpperCase();
        if (elemName == 'SELECT') {
            var o = new Option(newRepr, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
        }
        else 
            if (elemName == 'INPUT') {
                if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
                    elem.value += ',' + newId;
                }else {
                    if (name == "id_fornitore") {
                        $.post("/get-ragione-sociale-by-id", {
                            id: newId,
                            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                        }).done(function(data){
                            destination.val(data);
                            destination = null;
                        });
                    } else if ((name.indexOf("id_righe_fattura_acquisto-")==0) && (name.indexOf("-prodotto")>=27)){
                        $.post("/get-nome-prodotto-by-id", {
                            id: newId,
                            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                        }).done(function(data){
                            destination.val(data);
                            destination = null;
                        });
                    } else if ((name.indexOf("id_righe_fattura_acquisto-")==0) && (name.indexOf("-unita_di_misura")>=27)){
                        $.post("/get-unita-di-misura-by-id", {
                            id: newId,
                            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                        }).done(function(data){
                            destination.val(data);
                            destination = null;
                        });
                    }
                }
            }
    }
    else {
        var toId = name + "_to";
        elem = document.getElementById(toId);
        var o = new Option(newRepr, newId);
        SelectBox.add_to_cache(toId, o);
        SelectBox.redisplay(toId);
    }
    win.close();
}

function calcola_totale_riga(obj){
    var prezzo = obj.parent().parent().find(".field-prezzo input").val();
    var quantita = obj.parent().parent().find(".field-quantita input").val();
    
    if (prezzo == "" || quantita == ""){
        return;
    }
    
    prezzo = parseFloat(prezzo.replace(",", "."));
    quantita = parseFloat(quantita.replace(",", "."));

    var totale = prezzo * quantita;
    
    totale = totale.toFixed(5);
    
    obj.parent().parent().find(".field-totale_riga input").val(totale);
};

function calcola_totale_fattura(){
    var totale = 0.0;
    $(".field-totale_riga input").each(function(){
        var totale_riga = $(this).val();
        if (totale_riga != ""){
            totale += parseFloat(totale_riga);
        }
    });
    
    $("#id_totale").val(totale.toFixed(5));
}

$(function(){
    $("#id_totale").attr("disabled", "disabled");
    $(".field-totale_riga input").attr("disabled", "disabled");
    
    append_addNew_button("fornitore", ".field-fornitore div");
    $(".field-prodotto").not("#righe_fattura_acquisto-empty .field-prodotto").each(function(index){
        append_addNew_button("prodotto", "#" + $(this).parent().attr("id")+ " .field-prodotto");
    });
    
    $(".field-unita_di_misura").not("#righe_fattura_acquisto-empty .field-unita_di_misura").each(function(index){
        append_addNew_button("unita_misura", "#" + $(this).parent().attr("id")+ " .field-unita_di_misura");
    });
    

    $("#id_fornitore").autocomplete({
        source: "/get-lista-fornitori/",
        minLength: 1,
    });
    
    $('#id_fornitore').keypress(function (e) {
        if (e.keyCode == 9) {
            $(this).trigger(jQuery.Event("keydown", { keyCode: 40 }));
        }
    });


    $(".dynamic-righe_fattura_acquisto .field-prodotto input").autocomplete({
        source: "/get-lista-prodotti/",
        minLength: 1,
    });
    $('.dynamic-righe_fattura_acquisto .field-prodotto input').keypress(function (e) {
        if (e.keyCode == 9) {
            $(this).trigger(jQuery.Event("keydown", { keyCode: 40 }));
        }
    });


    $(".dynamic-righe_fattura_acquisto .field-unita_di_misura input").autocomplete({
        source: "/get-lista-unita-misura/",
        minLength: 1,
    });
    
    $('.dynamic-righe_fattura_acquisto .field-unita_di_misura input').keypress(function (e) {
        if (e.keyCode == 9) {
            $(this).trigger(jQuery.Event("keydown", { keyCode: 40 }));
        }
    });


    $(".field-prezzo input[type='text']").not("#righe_fattura_acquisto-empty .field-prezzo input").each(function(index){
        calcola_totale_riga($(this));
        $(this).change(function(){
            calcola_totale_riga($(this))
            calcola_totale_fattura();
        });
    });
    
    $(".field-quantita input[type='text']").not("#righe_fattura_acquisto-empty .field-quantita input").each(function(index){
        $(this).change(function(){
            calcola_totale_riga($(this));
            calcola_totale_fattura();
        });
    });
    
    calcola_totale_fattura();
});