# Anonymous_psychological_support_service
#Служба анонимной психологической поддержки
Данное Django приложение является полноценным сайтов для службы анонимной психологической поддержки.
Реализован анонимный чат.
Так же на сейте реализованы блоки новостей, советов, и гороскоп. Реализована возможность добавления и редактирования этих разделов.
На сайте существует 2 роли.
1-Студент:
  Каждый зарегистрированный пользовател, определяется как студент.
  Он может создать беседу и его запрос будет отправлен в списке заявок, который видят только специалисты.
  После нахождения специалиста, общаться 
2-Специалист:
  Специалисту доступны все студенты, которые написали и пока им никто не ответил.
  После того, как специалист отвит студенту, студент привязывается к специалисту и другие специалисты не видят этого студента.
  Ни переписку, ни самого студента. Он исчезает из общего пула заявок, его может видеть только свой специалист.
  У специалиста создана страница диалогов - все студенты, с которыми он переписывается, приведены в этом странице.
  
/*/*/*/*/*/*/*//*/*/*/*//*/*//*//*/*/*/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

This Django application is a complete anonymous psychological support site.
Anonymous chat has been implemented.
Blocks of news, tips, and a horoscope are also implemented on the site. The ability to add and edit these sections has been implemented.
There are 2 roles on the site.
1-Student:
  Each registered user is identified as a student.
  He can create a conversation and his request will be sent to the list of requests, which is visible only to specialists.
  After finding a specialist, communicate
2-Specialist:
  The specialist has access to all students who have written and so far no one has answered them.
  After the specialist answers the student, the student becomes attached to the specialist and other specialists do not see this student.
  Neither correspondence, nor the student himself. It disappears from the general pool of applications; only your specialist can see it.
  The specialist has created a page of dialogues - all students with whom he corresponds are listed on this page.
