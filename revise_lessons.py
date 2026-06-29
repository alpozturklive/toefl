#!/usr/bin/env python3
"""
Comprehensive TOEFL lesson revision script.
1. Format cleanup for all lessons (1-9)
2. Sentence enrichment for lessons 6-9
3. Create new lessons 10-13
"""
import re
import os

BASE = "/Users/alparslanozturk/projects/toefl"

# ─── Phase 1: Format cleanup helpers ─────────────────────────────────────────

def fix_theme_title(line):
    """'## Tema N: Turkish (English)' → '## Tema N: English'"""
    m = re.match(r'^(## Tema \d+: ).+\((.+?)\)\s*$', line.rstrip())
    if m:
        return m.group(1) + m.group(2) + '\n'
    return line

def clean_lesson(content, lesson_num):
    lines = content.split('\n')
    cleaned = []
    for line in lines:
        # Skip Turkish intro blurbs
        if re.match(r'^> Bu dosyayı', line): continue
        if re.match(r'^> Sadece \*\*Listen', line): continue
        # Fix theme titles
        if re.match(r'^## Tema \d+:', line):
            line = fix_theme_title(line + '\n').rstrip()
        cleaned.append(line)
    content = '\n'.join(cleaned)

    # Remove Puanlama + Süre + Telaffuz block (keep footer starting with > **Toplam**)
    content = re.sub(
        r'\n## Puanlama.*?(?=\n---\n\n> \*\*Toplam)',
        '',
        content,
        flags=re.DOTALL
    )
    return content

# ─── Phase 2: New enriched sentences for lessons 6-9 ─────────────────────────

LESSON6_NEW = """\
# TOEFL 2026 — Ders 6: Student Organizations, Campus Events, Study Abroad

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: Student Organizations

1. Club membership is open to all enrolled students.
2. Applications for officer positions close at the end of the semester.
3. Weekly meetings are held every Tuesday in the student union.
4. New members must attend one orientation session before joining.
5. A club needs at least ten active members to stay registered.
6. Budget requests are submitted to the student government office.
7. Community service hours count toward club recognition each year.
8. All events must be approved by the student activities office first.
9. Club officers are elected by the general membership each spring.
10. Fundraising activities require prior approval from campus administration.
11. The student newspaper lists all upcoming registered club events.
12. Clubs that go inactive risk losing their official funding and status.
13. All student groups must renew their registration at the start of fall.
14. Volunteer openings are posted weekly on the student affairs board.
15. The student government awards funds to qualifying clubs each semester.

---

## Tema 2: Campus Events

16. Orientation week begins three days before the first day of classes.
17. Tickets for the spring concert are sold at the student union box office.
18. The cultural festival features food, music, and dance from around the world.
19. Graduation ceremonies are held in the main auditorium every May.
20. Public lectures are announced on the university website each week.
21. Parking fills up fast during large events, so take the campus shuttle.
22. The student union hosts an open mic night every Friday evening.
23. Campus tours for prospective students run Monday through Saturday.
24. Holiday events are organized by the international student services office.
25. Photography may be restricted at certain campus performances.
26. The career fair takes place twice a year in the main gymnasium.
27. Museum exhibits are free to students with a valid university ID.
28. Event volunteers earn community service credit toward their degree.
29. Weather cancellations are sent through the university alert system.
30. Please silence your phone before entering any campus performance space.

---

## Tema 3: Study Abroad

31. Applications for exchange programs are accepted twice per year.
32. Students must hold a minimum GPA to qualify for study abroad.
33. Financial aid can often apply to approved international programs.
34. A valid passport is required at least six months before departure.
35. Credit transfer rules depend on the policies of the host university.
36. All students studying abroad must carry valid health insurance.
37. The international office holds pre-departure sessions each semester.
38. Language requirements vary by program and destination country.
39. Housing abroad is typically arranged through the host institution.
40. Students must register their travel plans with the campus safety office.
41. A study abroad advisor can help you choose the right program.
42. Internship credit is available through approved international placements.
43. Some programs require all coursework to be completed in the local language.
44. Re-entry advising helps students readjust after returning to campus.
45. Scholarships for study abroad programs are listed on the financial aid page.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson5.md` → Science Lecture, Lab, Research
> **Sonraki:** `lesson7.md` → Technology, Online Classes, Financial Aid
"""

LESSON7_NEW = """\
# TOEFL 2026 — Ders 7: Campus Technology, Online Classes, Financial Aid

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: Campus Technology

1. The campus Wi-Fi is available in all academic buildings.
2. Students receive a university email account when they enroll.
3. The IT help desk is open weekdays from eight to six.
4. Microsoft Office is free to download for all enrolled students.
5. Printing credits are added to your student account each semester.
6. Computer labs are open for walk-in use during posted hours.
7. Personal devices must be registered to access the secure network.
8. All assignments are submitted through the learning management system.
9. You must verify your identity with two-factor authentication to log in.
10. Contact IT support by phone, email, or in person at the tech center.
11. Installing unauthorized software on lab computers is strictly prohibited.
12. Cloud storage is provided through the university student portal.
13. Cybersecurity workshops run each semester through the IT department.
14. Back up your academic work regularly — the university is not responsible for lost files.
15. Assistive technology tools are available for students with disabilities.

---

## Tema 2: Online & Hybrid Classes

16. Course materials for the week are posted every Sunday evening.
17. Discussion board posts count toward your overall course grade.
18. Watch all video lectures before the weekly live session begins.
19. Report any technical problems to your instructor right away.
20. A webcam is required for all proctored online exams.
21. Check time zone differences before scheduling live class sessions.
22. Online students have full access to the digital library and databases.
23. Assignment deadlines are the same regardless of course format.
24. Hybrid courses meet in person twice a week and online for the rest.
25. Test your audio and video before each virtual class session.
26. Use the chat feature respectfully during live sessions.
27. Office hours for online courses are held by video call.
28. Course evaluations are submitted online at the end of each term.
29. Academic honesty rules apply equally to online and in-person courses.
30. Log in and participate actively every week to stay on track.

---

## Tema 3: Financial Aid

31. The financial aid application must be submitted before the deadline.
32. Scholarships are awarded based on both merit and financial need.
33. Aid packages are reviewed and renewed at the start of each academic year.
34. You must make satisfactory academic progress to keep your aid.
35. Work-study positions are listed through the financial aid office.
36. Loan repayment starts six months after you graduate or withdraw.
37. The financial aid office holds information sessions every fall semester.
38. Outside scholarships must be reported to the financial aid office.
39. Grants do not need to be paid back, unlike student loans.
40. You can appeal for more aid by submitting supporting documents.
41. Emergency funds are available for students facing sudden hardship.
42. The estimated cost of attendance includes tuition, housing, and living expenses.
43. Aid recipients must enroll in a minimum number of credit hours each term.
44. Tax documents related to your scholarships are mailed early each year.
45. Financial literacy workshops help students manage budgets and student debt.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson6.md` → Student Organizations, Campus Events, Study Abroad
> **Sonraki:** `lesson8.md` → Registrar, Academic Advising, Tutoring Center
"""

LESSON8_NEW = """\
# TOEFL 2026 — Ders 8: Registrar, Academic Advising, Tutoring Center

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: Registrar's Office

1. Course registration opens two weeks before each semester begins.
2. Meet with your advisor before registering for any new classes.
3. A hold on your account will block you from enrolling in courses.
4. Request official transcripts through the registrar's online portal.
5. The deadline to add or drop a course is the end of week two.
6. Withdrawing after the deadline leaves a W on your transcript.
7. Enrollment verification letters are available at the registrar's office.
8. Your degree audit shows exactly which graduation requirements you have met.
9. Name and address changes must be submitted in writing to the registrar.
10. Full-time status requires a minimum of twelve credit hours per semester.
11. Incomplete grades must be resolved within one semester of the course ending.
12. Enrolling in more than eighteen hours requires written approval.
13. Final grades are posted to the student portal two weeks after the semester ends.
14. Transfer credits are reviewed by both the registrar and the relevant department.
15. The academic calendar lists all important registration dates for the year.

---

## Tema 2: Academic Advising

16. Schedule an advising appointment through the online booking system.
17. Meet with your advisor at least once each semester.
18. A GPA below 2.0 places a student on academic probation.
19. Changing your major requires written approval from both departments.
20. Complete all prerequisites before enrolling in upper-division courses.
21. Your advisor can help you build a schedule that meets graduation requirements.
22. Talk to an advisor early if you are considering graduate school.
23. An advising hold means you must meet before registration opens.
24. Transfer students should schedule an advising appointment in their first week.
25. The advising center is open Monday through Friday during business hours.
26. You may request a new advisor when you change your major.
27. Course substitutions and waivers must be approved by the advising office.
28. Double majors must meet the requirements of each program separately.
29. Students on academic warning should contact their advisor right away.
30. Four-year degree plans help you stay on track toward graduation.

---

## Tema 3: Tutoring & Writing Center

31. Tutoring is available free of charge to all currently enrolled students.
32. Book tutoring appointments online up to one week in advance.
33. Walk-in sessions are offered on weekday afternoons during peak hours.
34. The writing center gives feedback on drafts, not final proofreading.
35. Bring your assignment guidelines when you visit the writing center.
36. Group tutoring is available for introductory math and science courses.
37. Tutors are trained students from across the academic departments.
38. The tutoring center is on the second floor of the student services building.
39. Online tutoring is available for students in fully remote programs.
40. Students who use tutoring regularly tend to perform better over time.
41. The writing center helps improve clarity and organization in your papers.
42. Missing an appointment without notice will result in a temporary hold.
43. Request a tutor who specializes in the subject area you need most.
44. Weekly group review sessions are offered for difficult core courses.
45. All tutoring services are confidential and designed to support your success.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson7.md` → Technology, Online Classes, Financial Aid
> **Sonraki:** `lesson9.md` → Campus Housing, Campus Safety, Campus Transit
"""

LESSON9_NEW = """\
# TOEFL 2026 — Ders 9: Campus Housing, Campus Safety, Campus Transit

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: Campus Housing Office

1. Housing applications for fall semester open in early March.
2. Submit roommate preferences through the online housing portal before the deadline.
3. Residence hall contracts cover the full academic year.
4. Early move-in before the official date is available for an extra fee.
5. Room changes are not allowed during the first two weeks of the semester.
6. Overnight guests may stay for no more than three nights in a row.
7. Quiet hours run from ten at night until eight in the morning on weekdays.
8. Show your student ID to enter any campus residence hall after hours.
9. Cooking is only allowed in the designated kitchen areas of each building.
10. Report maintenance issues through the online work order system promptly.
11. The housing office assigns rooms by the date your application was received.
12. Students who want to live off campus must notify the housing office in writing.
13. University furniture may not be removed from residence hall rooms.
14. Fire safety inspections can happen at any time without prior notice.
15. Check out with your residential advisor before any extended break.

---

## Tema 2: Campus Safety

16. The campus safety office is open twenty-four hours a day, seven days a week.
17. Emergency call boxes are placed at regular intervals across campus.
18. Report any suspicious activity to campus safety right away.
19. Lost or stolen property should be reported to campus safety as soon as possible.
20. Safety officers patrol all parking lots and academic buildings regularly.
21. The safe walk program provides student escorts across campus at night.
22. Bicycles must be registered and locked to designated racks only.
23. Alcohol is not allowed in common areas or residence hall corridors.
24. All campus incidents are reviewed by the safety committee each month.
25. Emergency alerts are sent to all registered phones through the campus system.
26. First aid kits are mounted in every academic building near the main stairwells.
27. Sign up for the campus emergency notification system to stay informed.
28. Campus safety works closely with local police on serious incidents.
29. Call the campus safety office to request an escort to your vehicle.
30. Security cameras monitor all public areas of the university continuously.

---

## Tema 3: Campus Transit

31. The campus shuttle runs every fifteen minutes on weekdays.
32. Bus schedules are posted at each stop and updated in the transit app.
33. A valid university ID gets you a free ride on all campus shuttles.
34. The last shuttle leaves the main terminal at midnight on weeknights.
35. Extended shuttle service runs during finals week and major campus events.
36. Bike-sharing stations are located near the main library and the student union.
37. Carpooling programs are coordinated through the campus transportation office.
38. A valid parking permit is required for all vehicles on campus.
39. Accessible parking spaces require a valid placard or university permit.
40. The transit office offers a subsidized city bus pass to enrolled students.
41. Shuttle routes and schedules may change at the start of each semester.
42. Track shuttle locations in real time using the university mobile app.
43. Please give priority seating to passengers with disabilities or heavy loads.
44. Scooters and skateboards are not allowed inside campus buildings.
45. Report shuttle delays or disruptions using the online transit feedback form.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson8.md` → Registrar, Academic Advising, Tutoring Center
> **Sonraki:** `lesson10.md` → IT Help Desk, Computer Lab, Campus Parking
"""

# ─── Phase 3: New lessons 10-13 ───────────────────────────────────────────────

LESSON10_NEW = """\
# TOEFL 2026 — Ders 10: IT Help Desk, Computer Lab, Campus Parking

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy + goarno.io practice scenarios

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: IT Help Desk

1. Welcome to the IT help desk.
2. Please have your student ID ready.
3. Laptops can be borrowed for up to three days.
4. You must connect to the secure student network.
5. Software updates run automatically every weekend.
6. If you forget your password, use the self-service portal to reset it.
7. Late equipment returns result in a temporary suspension of your borrowing privileges.
8. We can help you connect to the campus network.
9. Please restart your laptop before we run any diagnostics.
10. Enter your university email address to access the system.
11. The password is the same one you use for course registration.
12. Wireless internet is available in all classroom buildings on campus.
13. If your device keeps disconnecting, you may need to update your operating system.
14. Students can download free antivirus software from the main technology portal.
15. Contact the IT office by phone, email, or walk-in during business hours.

---

## Tema 2: Computer Lab

1. Welcome to the main computer lab.
2. Please sign in at the front desk.
3. Color printing costs ten cents per page.
4. You must have a valid student ID to log in to any computer.
5. Do not leave your personal belongings unattended in the lab.
6. If you need help with the software, ask the assistant at the main desk.
7. The lab stays open twenty-four hours during the final exam period.
8. Save your work to an external drive — computers clear all data daily.
9. Technical support staff is on duty at the front counter until midnight.
10. You can book a private workstation on the university website in advance.
11. Food and drinks are not allowed near the machines to protect the equipment.
12. Printing requires a positive balance on your student account.
13. Do not save personal files on the lab desktops.
14. Log out completely when you finish to protect your account.
15. Software on these machines is updated automatically every Sunday night.

---

## Tema 3: Campus Parking

1. Bring your student ID to the front desk to apply for a parking permit.
2. Complete the parking application online before visiting the office.
3. Park only in the zones assigned to your specific permit type.
4. Place the permit sticker on the lower left corner of your windshield.
5. Commuter students may not leave their cars overnight in the main lot.
6. If you lose your parking pass, pay the replacement fee before getting a new one.
7. Visitors should buy a daily pass from the kiosk near the main campus entrance.
8. All vehicles must display a valid permit during posted enforcement hours.
9. Illegally parked vehicles will be ticketed and may be towed.
10. Handicapped spaces require a state-issued placard or university permit.
11. Permit fees are charged to your student account at the start of each semester.
12. Report damaged parking meters or gate malfunctions to the transit office.
13. Carpooling permits are available at a reduced rate through the transportation office.
14. Electric vehicle charging stations are located in lots B and D.
15. The transit office is open weekdays from seven in the morning until six in the evening.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson9.md` → Campus Housing, Campus Safety, Campus Transit
> **Sonraki:** `lesson11.md` → Fitness Center, Sports Center, Recreation
"""

LESSON11_NEW = """\
# TOEFL 2026 — Ders 11: Fitness Center, Sports Center, Recreation

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy + goarno.io practice scenarios

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: Campus Fitness Center

1. Welcome to the fitness center.
2. Please scan your student ID at the entrance.
3. Athletic shoes must be worn at all times on the gym floor.
4. Wipe down every machine after you finish using it.
5. Group exercise classes are held on the second floor each evening.
6. If you need help with the free weights, ask a personal trainer for guidance.
7. Lockers are available in the changing rooms, but you must bring your own lock.
8. Only water bottles with secure lids are allowed in the workout area.
9. Group fitness classes require registration through the campus app.
10. Equipment such as resistance bands can be checked out at the front desk.
11. Please return all weights to their proper racks before leaving the facility.
12. Personal training sessions can be scheduled online at a discounted student rate.
13. The pool is located on the ground floor and opens at six in the morning.
14. Swim lanes must be reserved online at least one day in advance.
15. The fitness center closes at eleven on weeknights and at eight on weekends.

---

## Tema 2: Community Sports Center

1. Thank you for joining the campus sports center.
2. Please wear clean, non-marking shoes inside all courts.
3. The swimming pool is on the ground floor of the building.
4. Members must wipe down equipment after every use.
5. Group fitness classes run every evening of the week.
6. To play tennis, reserve a court online at least twenty-four hours ahead.
7. Store your personal items in the locker room to keep them safe.
8. Basketball courts can be reserved online up to forty-eight hours in advance.
9. Lockers are available for daily use and require a coin deposit.
10. If you lose your membership card, a replacement can be printed at the front desk.
11. Group sports leagues are organized each semester through the intramural office.
12. Guests may use the facility for a daily fee when accompanied by a member.
13. All members must sign a liability waiver before using the climbing wall.
14. The indoor track is open for general use when no events are scheduled.
15. Childcare services are available in the east wing during morning hours.

---

## Tema 3: Campus Recreation Programs

1. Welcome to the campus recreation center.
2. Please sign in at the front desk each time you visit.
3. The indoor pool opens at six-thirty on weekday mornings.
4. Lockers are available for daily use only — do not leave items overnight.
5. All group fitness classes require advance registration through the app.
6. If you plan to use the weight room, bring a clean towel with you.
7. Indoor basketball courts can be reserved online up to two days in advance.
8. The recreation center offers yoga, spin, and aqua aerobics each week.
9. Outdoor adventure trips are organized monthly through the rec office.
10. Kayak and camping gear can be rented from the outdoor equipment room.
11. Weekend climbing trips are posted on the recreation center bulletin board.
12. Intramural sports registration opens at the beginning of each semester.
13. All participants in contact sports must wear the provided protective gear.
14. The recreation staff can help you find an activity that fits your schedule.
15. Student recreation memberships are included in the semester activity fee.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson10.md` → IT Help Desk, Computer Lab, Campus Parking
> **Sonraki:** `lesson12.md` → Chemistry Lab, Biology Lab, Robotics Open House
"""

LESSON12_NEW = """\
# TOEFL 2026 — Ders 12: Chemistry Lab, Biology Lab, Robotics Open House

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy + goarno.io practice scenarios

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: Chemistry Lab Safety

1. Please put on your safety goggles before entering the lab.
2. Food and drinks are never allowed inside the laboratory.
3. All chemical spills must be reported to the instructor immediately.
4. Wash your hands thoroughly before leaving the lab area.
5. Broken glass must be placed in the designated sharps container.
6. You are required to wear a lab coat and closed-toe shoes at all times.
7. In an emergency, use the eye wash station near the front exit.
8. Store all chemical reagents in their proper labeled containers after use.
9. Ventilation must be running whenever you work with volatile substances.
10. Label every sample container clearly with your name and the date.
11. Dispose of chemical waste in the correct bins posted above each station.
12. Review the safety data sheet for any new chemical before you begin.
13. Tie back long hair and remove loose jewelry before starting an experiment.
14. Never pipette by mouth — always use a mechanical pipetting device.
15. Report any unusual odors or equipment malfunctions to the lab supervisor.

---

## Tema 2: Biology Lab Safety

1. Safety goggles must be worn at all times in this laboratory.
2. Tie back long hair before handling any specimens or equipment.
3. Always wash your hands thoroughly before leaving the room.
4. Broken glass should go directly in the red sharps bin near the door.
5. Do not eat or drink at your workstations under any circumstances.
6. If you spill a chemical, notify the instructor immediately and step back.
7. Make sure all microscopes are turned off and unplugged before you leave.
8. Gloves are provided at the supply station near the main entrance.
9. Results must be reviewed and signed by the lab instructor before you leave.
10. The lab is open for independent research only during posted hours.
11. Return all reagents to their proper storage locations after use.
12. Students are paired in groups of two for all experimental procedures.
13. Record all data in the official lab notebook using ink, not pencil.
14. Dispose of biological materials in the labeled biohazard bags only.
15. Complete the online safety quiz before attending your first lab session.

---

## Tema 3: Robotics Lab Open House

1. Welcome to the robotics open house.
2. Please leave your backpacks near the door when you enter.
3. You must wear safety glasses inside the testing and demonstration area.
4. Please do not touch any equipment or projects on the display tables.
5. Feel free to ask the student engineers about their current projects.
6. If you are interested in joining the team, speak with the lead researcher.
7. After the main floor tour, we will move to the software design room.
8. The robotics club meets every Wednesday evening in this building.
9. Membership applications open at the start of each academic semester.
10. Students from any major are welcome to join the engineering team.
11. The club competes in regional and national robotics competitions each year.
12. Sponsors and industry partners are often present at open house events.
13. Photography of the demonstration robots is permitted in the main hall only.
14. Refreshments are available in the lobby after the guided tour ends.
15. Sign the attendance sheet near the entrance to receive your participation credit.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson11.md` → Fitness Center, Sports Center, Recreation
> **Sonraki:** `lesson13.md` → Museum, Botanical Garden, Observatory
"""

LESSON13_NEW = """\
# TOEFL 2026 — Ders 13: Museum Tour, Botanical Garden, Observatory

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy + goarno.io practice scenarios

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: Museum Tour

1. Please gather near the entrance before the guided tour begins.
2. The tour starts in just a few minutes.
3. Make sure your headset is working before we begin walking.
4. Photography is permitted in the main hall only.
5. This exhibit covers three thousand years of human history.
6. Please stay close to the group so everyone can hear the guide clearly.
7. Large bags and backpacks must be stored in the lockers near the front desk.
8. Tonight we will screen three short documentary films in the theater.
9. The directors will answer audience questions after the final screening.
10. You can vote for the audience award at the table in the main lobby.
11. A short break will take place between the second and third films.
12. Keep your ticket stub — you will need it for tomorrow's panel discussion.
13. Touching the exhibits or display cases is strictly prohibited.
14. Guided tours are offered daily at ten, noon, and three in the afternoon.
15. The museum gift shop is open until thirty minutes after closing time.

---

## Tema 2: Botanical Garden

1. Welcome to the botanical garden.
2. Please stay on the marked paths at all times.
3. Do not touch any of the tropical plants in this room.
4. Some rare species require high humidity and must not be disturbed.
5. The back research section is closed to general visitors.
6. If you take photographs of the plants, please turn off your camera flash.
7. Guided tours are available every afternoon — register at the main entrance.
8. The tropical greenhouse is straight ahead on your right.
9. Many rare species bloom during the spring season here.
10. Information labels are placed near the base of each major plant.
11. If you want to take photos, make sure not to block the path for others.
12. Guided tours start every hour from the visitor center near the main gate.
13. Please do not pick flowers or remove any plant material from the garden.
14. The garden café serves light meals from ten in the morning until four.
15. Touching the delicate flowers can transfer oils from your skin to the petals.

---

## Tema 3: University Observatory

1. Welcome to the university observatory.
2. The tour will begin in just a moment.
3. Please give your eyes a few minutes to adjust to the darkness.
4. The main telescope is housed in the dome at the top of this building.
5. Tonight we will be viewing Jupiter and its four largest moons.
6. Do not use your phone camera — the bright screen will ruin your night vision.
7. If clouds move in, we will go downstairs to watch a solar system documentary.
8. The planetarium opens at sunset each evening throughout the semester.
9. Tickets are sold at the front gate and online in advance.
10. Please silence all mobile devices before entering the domed theater.
11. You can view the rings of Saturn clearly through the main telescope tonight.
12. If the sky stays clear, we may also spot a few distant star clusters.
13. Visitors must remain seated until the house lights come back on fully.
14. After the presentation, the guest astronomer will take questions in the lobby.
15. School group visits must be booked at least two weeks ahead of the visit date.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson12.md` → Chemistry Lab, Biology Lab, Robotics Open House
> **Sonraki:** `lesson14.md` → Airport Gate, Campus Mailroom, Career Center
"""

LESSON14_NEW = """\
# TOEFL 2026 — Ders 14: Airport Gate, Campus Mailroom, Career Center

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy + goarno.io practice scenarios

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: Airport Departure Gate

1. Welcome to gate number five.
2. Please have your boarding pass ready to scan.
3. We will begin boarding in approximately ten minutes.
4. Passengers with priority seating may board the plane first.
5. Make sure all personal items fit under the seat in front of you.
6. If your carry-on bag is too large, we can check it at the gate for free.
7. Thank you for your patience while we prepare the aircraft for departure.
8. Please have your passport ready when you approach the boarding desk.
9. Passengers traveling with small children may board at this time.
10. All carry-on bags must fit in the overhead bin or under the seat.
11. Remaining rows will begin boarding in just a few minutes.
12. Please gather all your personal belongings before walking down the jet bridge.
13. The estimated flight time to our destination is three hours and twenty minutes.
14. Electronic devices must be switched to airplane mode before takeoff.
15. The flight attendants will demonstrate the safety procedures shortly after boarding.

---

## Tema 2: Campus Mailroom

1. Welcome to the student mailroom.
2. Please have your student ID ready before approaching the counter.
3. All incoming packages are scanned and logged at the front desk.
4. You will receive an email notification when your package arrives.
5. All outgoing letters should be dropped in the blue collection bin.
6. Fragile items must be wrapped securely before you bring them to the counter.
7. If you lose your mailbox key, request a replacement online through the portal.
8. Large packages that do not fit in your mailbox are held at the front counter.
9. International shipping forms are available at the customer service window.
10. Packages are held for up to fourteen days before being returned to the sender.
11. Priority and express mail services are available for an additional fee.
12. The mailroom is open Monday through Friday from eight to five.
13. Saturday hours are limited — the mailroom closes at noon on weekends.
14. Students living off campus may use a PO box for a small annual fee.
15. All mail and packages are sorted and distributed by noon each weekday.

---

## Tema 3: Career Center Job Fair

1. Welcome to the career center.
2. Please take a copy of today's company schedule from the table.
3. Bring multiple printed copies of your resume to hand out to employers.
4. Professional clothing is strongly recommended for all visitors today.
5. Company representatives are here to answer your questions directly.
6. Schedule a practice interview online before the main event begins.
7. Research the participating employers in advance to make a strong impression.
8. Name tags are available at the registration desk near the main entrance.
9. The career fair runs from ten in the morning until four in the afternoon.
10. Employers are looking for candidates in engineering, finance, and healthcare.
11. Many companies will conduct on-site interviews at the fair today.
12. Collect business cards from company representatives for follow-up emails.
13. Drop your resume in the box at each company table for future openings.
14. A workshop on networking skills runs in room two-twelve at eleven o'clock.
15. Post-fair feedback forms are available at the career center front desk.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson13.md` → Museum Tour, Botanical Garden, Observatory
> **Sonraki:** `lesson15.md` → Dining Hall, Campus Store, Campus Tour
"""

LESSON15_NEW = """\
# TOEFL 2026 — Ders 15: Dining Hall, Campus Store, Campus Tour

> Kaynak: TOEFL iBT 2026 — Inspire SpeakEasy + goarno.io practice scenarios

---

## Başlangıç Komutu (AI'ya yapıştır)

```
Bu dosyadaki cümleleri bana sırayla, teker teker ver. Her seferinde:
1. Sadece bir cümle yaz — hepsini birden verme.
2. Ben cümleyi sesli tekrar ederim (veya yazarım).
3. Telaffuz, vurgu ve düşünce grupları hakkında kısa geri bildirim ver.
4. "a/an/the" gibi küçük kelimeleri ve sondaki -s/-ed eklerini kontrol et.
5. "Hazırım" veya "Next" dediğimde bir sonraki cümleye geç.
Tema 1'den başla.
```

---

## Tema 1: Campus Dining Hall

1. Welcome to the main dining hall.
2. Please swipe your student ID card at the entrance.
3. The salad bar is located in the center of the room.
4. Vegetarian options are marked with a green leaf symbol at each station.
5. You may take one piece of fruit when you leave the dining hall.
6. During busy hours, please share tables with other students.
7. Return all dishes and silverware to the washing station near the exit.
8. Hot meals are prepared fresh throughout the day at the main stations.
9. Breakfast runs from seven to ten, with both hot and cold options available.
10. We accept meal cards, credit cards, and mobile payments at all registers.
11. Gluten-free and allergen-aware options are labeled clearly at each station.
12. Please take only what you plan to eat to reduce food waste.
13. The weekly menu is posted every Sunday on our website and mobile app.
14. Trays and utensils must be returned to the designated return area after meals.
15. The dining hall is open seven days a week from seven in the morning until ten at night.

---

## Tema 2: Campus Bookstore & Store

1. Welcome to the campus bookstore.
2. Textbooks for your courses are organized by department in the back section.
3. You will find notebooks, pens, and supplies along the left wall.
4. Buybacks are accepted during finals week at the end of each semester.
5. Digital course materials can be purchased using your student login.
6. If a textbook is sold out, you can place an order at the front counter.
7. Returns are accepted within seven days with the original receipt and packaging.
8. University branded clothing and accessories are displayed near the entrance.
9. Popular items include hoodies, caps, and mugs featuring the school logo.
10. Seasonal and limited-edition items are available at the start of each term.
11. The store offers a price match guarantee on all required textbook titles.
12. Used textbooks are available at a significant discount while supplies last.
13. New designs and merchandise arrive at the beginning of each academic year.
14. Gift cards for the campus store are sold at the main checkout counter.
15. Student employees staff the store and can help you locate any item.

---

## Tema 3: Campus Tour

1. Welcome to the campus tour — we are glad you are here today.
2. Each tour sets off from the student union building at the top of the hour.
3. On your left is the biology building, which was renovated last summer.
4. Across the courtyard is the dining hall, open from seven in the morning until ten at night.
5. The fitness center is free for all enrolled students, including weekend access.
6. Buses to downtown leave from this stop every fifteen minutes on weekdays.
7. Please pick up a campus map from the information desk before we finish the tour.
8. The main library is straight ahead — it holds over two million volumes.
9. The student union houses the career center, food court, and student government offices.
10. Residence halls are located on the east side of campus near the sports complex.
11. The health center is open weekdays from eight in the morning until six in the evening.
12. Metered street parking is available along the north boundary of campus.
13. If you have questions during the tour, please raise your hand at any time.
14. At the end, you will have a chance to meet current students and ask questions.
15. Thank you for visiting — we hope to see you here as a student next fall.

---

> **Toplam:** 45 cümle — 3 tema
> **Önceki:** `lesson14.md` → Airport Gate, Campus Mailroom, Career Center
> **Sonraki:** Tamamlandı — 675 cümle hazır (ders1–15)
"""

# ─── Main execution ───────────────────────────────────────────────────────────

def process_lessons_1_5():
    """Apply format cleanup to lessons 1-5 (no sentence changes)."""
    # Lesson 1 special: fix header + footer reference
    path = f"{BASE}/lesson1.md"
    with open(path) as f:
        c = f.read()
    # Fix header
    c = c.replace(
        '# TOEFL 2026 — Ders 1: Listen & Repeat',
        '# TOEFL 2026 — Ders 1: Campus Dining, Campus Store, Lecture Hall'
    )
    # Remove intro blurbs
    c = re.sub(r'> Bu dosyayı .+?\n', '', c)
    c = re.sub(r'> Sadece .+?\n', '', c)
    # Fix theme titles
    def fix_t(m):
        prefix = m.group(1)
        rest = m.group(2)
        eng = re.search(r'\((.+?)\)', rest)
        return (prefix + eng.group(1)) if eng else m.group(0)
    c = re.sub(r'(## Tema \d+: )(.+)', fix_t, c)
    # Remove Puanlama + Telaffuz sections
    c = re.sub(r'\n## Puanlama.*?(?=\n---\n\n> \*\*Toplam)', '', c, flags=re.DOTALL)
    # Fix old footer reference
    c = c.replace('`ders002.md` → Kütüphane, Teknoloji Konferansı, Kariyer Forumu',
                  '`lesson2.md` → Library, Career Forum, MBA Open House')
    c = c.replace('> **Toplam:** 45 cümle — 3 kampüs teması',
                  '> **Toplam:** 45 cümle — 3 tema')
    with open(path, 'w') as f:
        f.write(c)
    print(f"✅ lesson1.md — format cleaned + header fixed")

    for n in range(2, 6):
        path = f"{BASE}/lesson{n}.md"
        with open(path) as f:
            c = f.read()
        c = re.sub(r'> Bu dosyayı .+?\n', '', c)
        c = re.sub(r'> Sadece .+?\n', '', c)
        c = re.sub(r'(## Tema \d+: )(.+)', fix_t, c)
        c = re.sub(r'\n## Puanlama.*?(?=\n---\n\n> \*\*Toplam)', '', c, flags=re.DOTALL)
        with open(path, 'w') as f:
            f.write(c)
        print(f"✅ lesson{n}.md — format cleaned")

def write_new_lessons():
    lessons = {
        6: LESSON6_NEW, 7: LESSON7_NEW, 8: LESSON8_NEW,
        9: LESSON9_NEW, 10: LESSON10_NEW, 11: LESSON11_NEW,
        12: LESSON12_NEW, 13: LESSON13_NEW, 14: LESSON14_NEW,
        15: LESSON15_NEW,
    }
    for n, content in lessons.items():
        path = f"{BASE}/lesson{n}.md"
        with open(path, 'w') as f:
            f.write(content)
        print(f"✅ lesson{n}.md — {'enriched + rewritten' if n <= 9 else 'new lesson created'}")

if __name__ == '__main__':
    print("=== Phase 1: Format cleanup for lessons 1-5 ===")
    process_lessons_1_5()
    print("\n=== Phase 2+3: Enrich lessons 6-9 + create lessons 10-15 ===")
    write_new_lessons()
    print("\n🎉 All done! Lessons 1-15 ready.")
