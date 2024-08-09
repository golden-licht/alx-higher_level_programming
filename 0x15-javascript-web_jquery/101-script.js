$(document).ready(function () {
  const newItem = '<li>Item</li>';
  const ul = $('UL.my_list');

  $('DIV#add_item').click(function () {
    ul.append(newItem);
  });

  $('DIV#remove_item').click(function () {
    const lastItem = ul.children(':last-child');
    lastItem.remove();
  });

  $('DIV#clear_list').click(function () {
    ul.children().remove();
  });
});
