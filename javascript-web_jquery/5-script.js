$('#add_item').click(function() {
  const ele = $('<li></li>');
  ele.text('Item');
  $('.my_list').append(ele);
})