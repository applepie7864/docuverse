css = '''
<style>
.chatbox {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.user {
    background-color: #2b313e
}
.bot {
    background-color: #475063
}
.avatar {
  width: 20%;
}
.avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

user_template = '''
<div class="chatbox user">
    <div class="avatar">
        <img src="https://i.pinimg.com/1200x/6b/f6/2c/6bf62c6c123cdcd33d2d693782a46b34.jpg">
    </div>    
    <div class="message">{{question}}</div>
</div>
'''

bot_template = '''
<div class="chatbox bot">
    <div class="avatar">
        <img src="https://media.istockphoto.com/id/1367545305/vector/artificial-intelligence-silhouette-vector-icons-isolated-on-white-cyber-technologies-icon.jpg?s=612x612&w=0&k=20&c=nkdmZgLC56BH6VNIshsukJfJhnqm6VbnB_Rb3TlvilI=">
    </div>
    <div class="message">{{answer}}</div>
</div>
'''