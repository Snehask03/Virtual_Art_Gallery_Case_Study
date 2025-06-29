class User:
    def __init__(self, user_id = None, user_name = None, user_password = None, email = None, first_name = None, last_name = None, date_of_birth = None, profile_picture = None, is_active = True):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_password = user_password
        self.__email = email
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__profile_picture = profile_picture
        self.__is_active = is_active

    def __str__(self):
        return (
            f"User [ID = {self.user_id}, User Name = '{self.user_name}',"
            f"Password = '{self.user_password}', Email = '{self.email}',"
            f"First Name = '{self.first_name}', Last Name = '{self.last_name}',"
            f"Date of Birth = {self.date_of_birth}, Profile Picture = '{self.profile_picture}' , Is Active = {self.is_active}]"
        )

    #Getters and Setters
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_name(self):
        return self.__user_name
    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    @property
    def user_password(self):
        return self.__user_password
    @user_password.setter
    def user_password(self, user_password):
        self.__user_password = user_password

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def date_of_birth(self):
        return self.__date_of_birth
    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    @property
    def profile_picture(self):
        return self.__profile_picture
    @profile_picture.setter
    def profile_picture(self, profile_picture):
        self.__profile_picture = profile_picture

    @property
    def is_active(self):
        return self.__is_active
    @is_active.setter
    def is_active(self, is_active):
        self.__is_active = is_active


