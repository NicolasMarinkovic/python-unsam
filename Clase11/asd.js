if ($v("P10400_SHOW_HIDE_DETALLES") == 0){
    var model = apex.region("entregas").widget().interactiveGrid("getViews", "grid").model;
    model.forEach(function(record) {                 
      if ($v("P10400_ID") == record[10]) {
        var col_cod_suc = model.getValue(record,"COD_SUC");
        var item_deleted = $v('P10400_DELETED');
        console.log(item_deleted.concat(col_cod_suc.concat(';')));	
        apex.item( "P10400_DELETED" ).setValue(item_deleted.concat(col_cod_suc.concat(';')));	
        console.log($v('P10400_DELETED'));
        var col_nroorden = model.getValue(record,"NROORDEN");
        var item_deleted = $v('P10400_DELETED');
        console.log(item_deleted.concat(col_nroorden.concat(';')));	
        apex.item( "P10400_DELETED" ).setValue(item_deleted.concat(col_nroorden.concat(';')));	
        console.log($v('P10400_DELETED'));
      } 
    });
  }


  model.forEach(function(record) {                 
    if ($v("P10400_ID") == record[10]) {
      var col_cod_suc = model.getValue(record,"COD_SUC");
      var item_deleted = $v('P10400_DELETED');
      console.log(typeof item_deleted);
      console.log(item_deleted);
      console.log(typeof col_cod_suc);
      console.log(col_cod_suc);
    } 
  });

  if ($v("P10400_SHOW_HIDE_DETALLES") == 0){
    var model = apex.region("entregas").widget().interactiveGrid("getViews", "grid").model;
    model.forEach(function(record, index, id) {        
      var modMeta = model.getRecordMetadata(id);            
      if (modMeta.deleted) {
      console.log("hola");
        var col_cod_suc = model.getValue(record,"COD_SUC");
        var item_deleted = $v('P10400_DELETED');
        apex.item( "P10400_DELETED" ).setValue(item_deleted.concat(col_cod_suc.concat(';')));
      console.log(item_deleted.concat(col_cod_suc.concat(';')))
        var col_nroorden = model.getValue(record,"NROORDEN");
        var item_deleted = $v('P10400_DELETED');
        apex.item( "P10400_DELETED" ).setValue(item_deleted.concat(col_nroorden.concat(';')));
      console.log(item_deleted.concat(col_nroorden.concat(';')))	
      } 
    });
  }