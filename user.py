class User:
    """
    Class that generates new users
    """
    user_list = []

    def __init__(self,username,password):
      self.username = username
      self.password = password

    # def save_user(self):
    #   '''
    #   save_user method saves the user objects into user_list
    #   '''
    #   User.user_list.append(self)      
