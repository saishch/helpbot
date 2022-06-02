
class Node :
    def __init__(self,question,keyword):
        self.question = question
        self.keyword = keyword
        self.list_child_node =[]

    def user_response(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node:
           if child.keyword in txt:
              child.user_response()

    def insert(self, node, question):
        if self.question == question :
            self.list_child_node.append(node)
        else:
            for child in self.list_child_node:
                child.insert(node,question)




first_question_racine = "quels sont vos besoin ? \n insérez un des mots clès \n pdf \n video "
question_one_pdf = "quel pdf aurais vous besoin ? \n python \n javascript"
question_one_video ="quel video aurais vous besoin \n python \n php \n javacript "


tree = Node("Dites help pour commencer","aide")

tree.insert(Node(first_question_racine,"help"),"Dites help pour commencer")
tree.insert(Node(question_one_pdf,"pdf"),first_question_racine)
tree.insert(Node(question_one_video,"video"),first_question_racine)


# choix reponse pdf
tree.insert(Node("ecrivez : python","python"),question_one_pdf)
tree.insert(Node("ecrivez : javascript","javascript"),question_one_pdf)

#choix reponse video
tree.insert(Node("ecrivez : python","python"),question_one_video)
tree.insert(Node("ecrivez : php","php"),question_one_video)
tree.insert(Node("ecrivez : javascript","javacript"),question_one_video)


current_path = [tree]



                