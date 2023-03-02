使用数据库：`sqlite3`



1. 创建表格：`my_database = sqlite3.connect('material.db')`。

2. 显示表格：使用HTML模板：

   ```html
   <table>
       <thead>
       <tr>
           {% for i in labels %}
               <td>{{ i }}</td>
           {% endfor %}
       </tr>
       </thead>
       <tbody>
       {% for i in content %}
           <tr>
               {% for j in i %}
                   <td>{{ j }}</td>
               {% endfor %}
           </tr>
       {% endfor %}
   
       </tbody>
   </table>
   ```

   `{% for i in labels %}` 是使用了 `python` 中的 `render_template`，将数据传给网页中显示。

   对应的 `python` 代码：

   ```python
   return render_template('test.html', content=content, labels=labels)
   ```

3. 修改表格：

   - 变为可修改

     这一部分是抄的。

     ```javascript
     (function(){
       $('input[type="button"]').on('click', function(){
         var $this = $(this),
           edit_status = $this.attr('edit_status'),
           status_value = edit_status && 1 == edit_status ? 0 : 1,
           $td_arr = $this.parent().prevAll('td');
         $this.val(1 == status_value ? '完成' : '编辑').attr('edit_status', status_value);
         $.each($td_arr, function(){
           var $td = $(this);
           if(1 == status_value) {
             $td.html('<input type="text" value="'+$td.html()+'">');
           } else if(0 == status_value){
             $td.html($td.find('input[type=text]').val());
           }
         });
       });
     })();
     ```

   - 提交修改

     大致代码如下：

     通过 `js` 获取前端表格内的消息，然后通过 `ajax` 发送给后端。

     ```javascript
     function upload_data(button) {
         var data = {
                     "学号":cells[0].innerHTML,
                     "姓名":cells[1].innerHTML,
                     "性别":cells[2].innerHTML,
                     "年级":cells[3].innerHTML,
                     "取向":cells[4].innerHTML,
                 };
     
         $.ajax({
                 type: "get",
                 url: "/edit",
                 data: data,
                 dataType: "json"
         });
     }
     ```

4. 删除表格：

   没做。

5. 添加表格：

   实现思路：首先添加一行，然后用户修改数据并提交。

   - 添加一行：

     大致代码：

     ```javascript
     for (var i = 0; i < 5; i++) {
         tr.appendChild(td);
     }
     tr.appendChild(edit_td);
     tr.appendChild(upload_td);
     document.getElementById('tsxt_info').appendChild(tr);
     ```
     
   - 提交（这里是新增而不是修改）：
   
     ```javascript
     $.ajax({
             type: "get",
             url: "/add",
             data: data,
             dataType: "json"
     });
     
     button.onclick = upload_data;
     button.text = "提交";
     ```
   
     
   
     ```javascript
     
     ```
   
     

