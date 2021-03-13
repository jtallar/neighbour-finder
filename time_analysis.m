# Take same M (M = 13, optimal?) with multiple N values.
# tc = f(N) With M = 13, periodic

N = 50;
# With same gen, optimal M = 13
times_50_onegen = [0.0008909702301025391, 0.0008757114410400391, 0.0008707046508789062, 0.0008814334869384766, 0.0008678436279296875];
# With different gens, optimal M = 13
times_50_multigen = [0.0008993148803710938, 0.0008730888366699219, 0.0008614063262939453, 0.0008833408355712891, 0.0009031295776367188];

N = 100;
# With same gen, optimal M = 13
times_100_onegen = [0.0014224052429199219, 0.0014274120330810547, 0.0014405250549316406, 0.0016224384307861328, 0.001422882080078125];
# With different gens, optimal M = 13
times_100_multigen = [0.0014376640319824219, 0.0014150142669677734, 0.0016105175018310547, 0.0014431476593017578, 0.0014188289642333984];

N = 300;
# With same gen, optimal M = 13
times_300_onegen = [0.004544496536254883, 0.004578590393066406, 0.004629611968994141, 0.004652261734008789, 0.004610300064086914];
# With different gens, optimal M = 13
times_300_multigen = [0.004681587219238281, 0.004517316818237305, 0.004582405090332031, 0.00459742546081543, 0.009050369262695312];

N = 500;
# With same gen, optimal M = 13
times_500_onegen = [0.010730504989624023, 0.010476350784301758, 0.011175870895385742, 0.010155677795410156, 0.010667085647583008];
# With different gens, optimal M = 13
times_500_multigen = [0.010246515274047852, 0.010392427444458008, 0.010454177856445312, 0.010222673416137695, 0.010287284851074219];

N = 700;
# With same gen, optimal M = 13
times_700_onegen = [0.016996383666992188, 0.017058134078979492, 0.017076492309570312, 0.017075538635253906, 0.017700672149658203];
# With different gens, optimal M = 13
times_700_multigen = [0.017558813095092773, 0.017472267150878906, 0.017743349075317383, 0.01739788055419922, 0.017412424087524414];

N = 850;
# With same gen, optimal M = 13
times_850_onegen = [0.024135828018188477, 0.0236508846282959, 0.02434992790222168, 0.02445673942565918, 0.02364969253540039];
# With different gens, optimal M = 13
times_850_multigen = [0.024128437042236328, 0.023890256881713867, 0.023960590362548828, 0.023895740509033203, 0.02412271499633789];

N = 1000;
# With same gen, optimal M = 13
times_1000_onegen = [0.03317117691040039, 0.033503055572509766, 0.03279733657836914, 0.03285408020019531, 0.03364157676696777];
# With different gens, optimal M = 13
times_1000_multigen = [0.032028913497924805, 0.032148122787475586, 0.032517194747924805, 0.03147411346435547, 0.03451371192932129];

N = 1200;
# With same gen, optimal M = 13
times_1200_onegen = [0.04375171661376953, 0.04347562789916992, 0.04407238960266113, 0.044231414794921875, 0.04500436782836914];
# With different gens, optimal M = 13
times_1200_multigen = [0.04444479942321777, 0.044365644454956055, 0.04319405555725098, 0.04403376579284668, 0.04340219497680664];

figure('name', "Execution time with M = 13 (optimal M), periodic - One generator")
x_list = [50, 100, 300, 500, 700, 850, 1000, 1200];
y_list = [mean(times_50_onegen), mean(times_100_onegen), mean(times_300_onegen), mean(times_500_onegen), mean(times_700_onegen), mean(times_850_onegen), mean(times_1000_onegen), mean(times_1200_onegen)];
delta_y_list = [std(times_50_onegen), std(times_100_onegen), std(times_300_onegen), std(times_500_onegen), std(times_700_onegen), std(times_850_onegen), std(times_1000_onegen), std(times_1200_onegen)];
errorbar(x_list, y_list, delta_y_list)
title("tc = f(N) with CIM");
xlabel("N");
ylabel("tc [s]");

figure('name', "Execution time with M = 13 (optimal M), periodic - Multiple generators")
y_list = [mean(times_50_multigen), mean(times_100_multigen), mean(times_300_multigen), mean(times_500_multigen), mean(times_700_multigen), mean(times_850_multigen), mean(times_1000_multigen), mean(times_1200_multigen)];
delta_y_list = [std(times_50_multigen), std(times_100_multigen), std(times_300_multigen), std(times_500_multigen), std(times_700_multigen), std(times_850_multigen), std(times_1000_multigen), std(times_1200_multigen)];
errorbar(x_list, y_list, delta_y_list)
title("tc = f(N) with CIM");
xlabel("N");
ylabel("tc [s]");

############################################################################################################
# Brute force with multiple N values.
# tc = f(N) With Brute force, periodic
N = 50;
# With same gen, Brute force
times_50_onegen = [0.002116680145263672, 0.0020987987518310547, 0.0020804405212402344, 0.002104520797729492, 0.0038475990295410156];

N = 100;
# With same gen, Brute force
times_100_onegen = [0.008200883865356445, 0.007828950881958008, 0.008628129959106445, 0.009889602661132812, 0.008105993270874023];

N = 300;
# With same gen, Brute force
times_300_onegen = [0.07070589065551758, 0.07041120529174805, 0.06978416442871094, 0.07054686546325684, 0.06952381134033203];

N = 500;
# With same gen, Brute force
times_500_onegen = [0.19370412826538086, 0.20225119590759277, 0.19970417022705078, 0.2126481533050537, 0.19982004165649414];

N = 700;
# With same gen, Brute force
times_700_onegen = [0.38848400115966797, 0.38538289070129395, 0.3838827610015869, 0.3936727046966553, 0.38204193115234375];

N = 850;
# With same gen, Brute force
times_850_onegen = [0.5614995956420898, 0.5659666061401367, 0.5713565349578857, 0.5593080520629883, 0.5564234256744385];

N = 1000;
# With same gen, Brute force
times_1000_onegen = [0.7806813716888428, 0.7983365058898926, 0.7735497951507568, 0.7951874732971191, 0.7857296466827393];

N = 1200;
# With same gen, Brute force
times_1200_onegen = [1.1155602931976318, 1.1370282173156738, 1.1342308521270752, 1.11159348487854, 1.1432347297668457];

figure('name', "Execution time with Brute Force, periodic - One generator")
x_list = [50, 100, 300, 500, 700, 850, 1000, 1200];
y_list = [mean(times_50_onegen), mean(times_100_onegen), mean(times_300_onegen), mean(times_500_onegen), mean(times_700_onegen), mean(times_850_onegen), mean(times_1000_onegen), mean(times_1200_onegen)];
delta_y_list = [std(times_50_onegen), std(times_100_onegen), std(times_300_onegen), std(times_500_onegen), std(times_700_onegen), std(times_850_onegen), std(times_1000_onegen), std(times_1200_onegen)];
errorbar(x_list, y_list, delta_y_list)
title("tc = f(N) with Brute force");
xlabel("N");
ylabel("tc [s]");

############################################################################################################
# Take multiple M + brute force with one N value.
# tc = f(M x M) With N = 500. M <= 13 because of condition
# Using onegen, same data for ALL, as previous results show similar values with more deviation
N = 500;

M = 0; # -> Brute force
# With same gen, brute force, periodic
times_brute_force_periodic = [0.19889497756958008, 0.19408798217773438, 0.20011138916015625, 0.19349455833435059, 0.19299840927124023];
# With same gen, brute force, not periodic
times_brute_force_not_periodic = [0.11092138290405273, 0.0983891487121582, 0.09909868240356445, 0.10026693344116211, 0.10122132301330566];

M = 1; # -> CIM
# With same gen, M = 1, periodic
times_m_1_periodic = [0.8223366737365723, 0.8115754127502441, 0.8365035057067871, 0.8398253917694092, 0.8119661808013916];
# With same gen, M = 1, not periodic
times_m_1_not_periodic = [0.09274649620056152, 0.09283280372619629, 0.09365391731262207, 0.09128308296203613, 0.09389281272888184];

M = 2; # -> CIM
# With same gen, CIM, periodic
times_m_2_periodic = [0.21058106422424316, 0.2094871997833252, 0.20670080184936523, 0.2036740779876709, 0.20656228065490723];
# With same gen, CIM, not periodic
times_m_2_not_periodic = [0.09002804756164551, 0.09160828590393066, 0.09143590927124023, 0.09331846237182617, 0.09473657608032227];

M = 3; # -> CIM
# With same gen, CIM, periodic
times_m_3_periodic = [0.09558415412902832, 0.09435033798217773, 0.09325647354125977, 0.09183645248413086, 0.09398698806762695];
# With same gen, CIM, not periodic
times_m_3_not_periodic = [0.056928396224975586, 0.05698084831237793, 0.05565452575683594, 0.05767059326171875, 0.05806374549865723];

M = 4; # -> CIM
# With same gen, CIM, periodic
times_m_4_periodic = [0.05635428428649902, 0.05556130409240723, 0.05450034141540527, 0.05563187599182129, 0.05490565299987793];
# With same gen, CIM, not periodic
times_m_4_not_periodic = [0.03940296173095703, 0.05025815963745117, 0.039886474609375, 0.03973722457885742, 0.03862261772155762];

M = 5; # -> CIM
# With same gen, CIM, periodic
times_m_5_periodic = [0.03757786750793457, 0.037201642990112305, 0.0358884334564209, 0.036989450454711914, 0.0367279052734375];
# With same gen, CIM, not periodic
times_m_5_not_periodic = [0.02844524383544922, 0.028493165969848633, 0.028018712997436523, 0.028220176696777344, 0.027840137481689453];

M = 6; # -> CIM
# With same gen, CIM, periodic
times_m_6_periodic = [0.027626991271972656, 0.02696967124938965, 0.02745962142944336, 0.0355219841003418, 0.029555320739746094];
# With same gen, CIM, not periodic
times_m_6_not_periodic = [0.0222628116607666, 0.02191781997680664, 0.02219390869140625, 0.023232698440551758, 0.022458314895629883];

M = 7; # -> CIM
# With same gen, CIM, periodic
times_m_7_periodic = [0.02096390724182129, 0.02130913734436035, 0.021642446517944336, 0.021495342254638672, 0.02151656150817871];
# With same gen, CIM, not periodic
times_m_7_not_periodic = [0.018856525421142578, 0.018410444259643555, 0.018358230590820312, 0.01794910430908203, 0.018154382705688477];

M = 8; # -> CIM
# With same gen, CIM, periodic
times_m_8_periodic = [0.017429113388061523, 0.017597198486328125, 0.0174257755279541, 0.017510652542114258, 0.017881155014038086];
# With same gen, CIM, not periodic
times_m_8_not_periodic = [0.015518903732299805, 0.015516519546508789, 0.015839338302612305, 0.01580977439880371, 0.015748023986816406];

M = 9; # -> CIM
# With same gen, CIM, periodic
times_m_9_periodic = [0.015110015869140625, 0.015326738357543945, 0.015321969985961914, 0.015766620635986328, 0.015229463577270508];
# With same gen, CIM, not periodic
times_m_9_not_periodic = [0.013553857803344727, 0.014635324478149414, 0.01354217529296875, 0.013753890991210938, 0.013668060302734375];

M = 10; # -> CIM
# With same gen, CIM, periodic
times_m_10_periodic = [0.01323699951171875, 0.013377189636230469, 0.013496637344360352, 0.01339268684387207, 0.013511896133422852];
# With same gen, CIM, not periodic
times_m_10_not_periodic = [0.011973857879638672, 0.011807918548583984, 0.012198209762573242, 0.012400627136230469, 0.01229715347290039];

M = 11; # -> CIM
# With same gen, CIM, periodic
times_m_11_periodic = [0.012019157409667969, 0.011816978454589844, 0.012233495712280273, 0.012086868286132812, 0.01212763786315918];
# With same gen, CIM, not periodic
times_m_11_not_periodic = [0.011103630065917969, 0.011066198348999023, 0.011237144470214844, 0.011023521423339844, 0.01092219352722168];

M = 12; # -> CIM
# With same gen, CIM, periodic
times_m_12_periodic = [0.011100530624389648, 0.011074542999267578, 0.010995626449584961, 0.01102447509765625, 0.011321067810058594];
# With same gen, CIM, not periodic
times_m_12_not_periodic = [0.010273933410644531, 0.01017618179321289, 0.010204553604125977, 0.010076761245727539, 0.010517120361328125];

M = 13; # -> CIM
# With same gen, CIM, periodic
times_m_13_periodic = [0.010181188583374023, 0.010443687438964844, 0.010122060775756836, 0.010092735290527344, 0.010295629501342773];
# With same gen, CIM, not periodic
times_m_13_not_periodic = [0.009809255599975586, 0.009679794311523438, 0.009540319442749023, 0.01059722900390625, 0.009660005569458008];

figure('name', "Execution time with N = 500, d=1.25 - Periodic active")
x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
y_list = [mean(times_m_1_periodic), mean(times_m_2_periodic), mean(times_m_3_periodic), mean(times_m_4_periodic), mean(times_m_5_periodic), mean(times_m_6_periodic), mean(times_m_7_periodic), mean(times_m_8_periodic), mean(times_m_9_periodic), mean(times_m_10_periodic), mean(times_m_11_periodic), mean(times_m_12_periodic), mean(times_m_13_periodic)];
delta_y_list = [std(times_m_1_periodic), std(times_m_2_periodic), std(times_m_3_periodic), std(times_m_4_periodic), std(times_m_5_periodic), std(times_m_6_periodic), std(times_m_7_periodic), std(times_m_8_periodic), std(times_m_9_periodic), std(times_m_10_periodic), std(times_m_11_periodic), std(times_m_12_periodic), std(times_m_13_periodic)];
errorbar(x_list, y_list, delta_y_list)
title("tc = f(M) and Brute force");
xlabel("M");
ylabel("tc [s]");
hold on
errorbar(x_list, repmat(mean(times_brute_force_periodic), 1, 13), repmat(std(times_brute_force_periodic), 1, 13))
hold off

# Con contornos periodicos, a partir de M=3, es mejor CIM que fuerza bruta

figure('name', "Execution time with N = 500, d=1.25 - Periodic INactive")
y_list = [mean(times_m_1_not_periodic), mean(times_m_2_not_periodic), mean(times_m_3_not_periodic), mean(times_m_4_not_periodic), mean(times_m_5_not_periodic), mean(times_m_6_not_periodic), mean(times_m_7_not_periodic), mean(times_m_8_not_periodic), mean(times_m_9_not_periodic), mean(times_m_10_not_periodic), mean(times_m_11_not_periodic), mean(times_m_12_not_periodic), mean(times_m_13_not_periodic)];
delta_y_list = [std(times_m_1_not_periodic), std(times_m_2_not_periodic), std(times_m_3_not_periodic), std(times_m_4_not_periodic), std(times_m_5_not_periodic), std(times_m_6_not_periodic), std(times_m_7_not_periodic), std(times_m_8_not_periodic), std(times_m_9_not_periodic), std(times_m_10_not_periodic), std(times_m_11_not_periodic), std(times_m_12_not_periodic), std(times_m_13_not_periodic)];
errorbar(x_list, y_list, delta_y_list)
title("tc = f(M) and Brute force");
xlabel("M");
ylabel("tc [s]");
hold on
errorbar(x_list, repmat(mean(times_brute_force_not_periodic), 1, 13), repmat(std(times_brute_force_not_periodic), 1, 13))
hold off

# Sin contornos periodicos, siempre es mejor CIM que fuerza bruta

############################################################################################################
# Take some M another N value.
# tc = f(M x M) With N = 1000. M <= 13 because of condition
# Using onegen, same data for ALL, as previous results show similar values with more deviation
N = 1000;

M = 2; # -> CIM
# With same gen, CIM, periodic
times_m_2_periodic = [0.8330726623535156, 0.8850812911987305, 0.8320260047912598, 0.8356661796569824, 0.8252713680267334];
# With same gen, CIM, not periodic
times_m_2_not_periodic = [0.3695342540740967, 0.376056432723999, 0.3771860599517822, 0.36344337463378906, 0.3791849613189697];

M = 5; # -> CIM
# With same gen, CIM, periodic
times_m_5_periodic = [0.14080810546875, 0.13909554481506348, 0.14325523376464844, 0.14111709594726562, 0.14478802680969238];
# With same gen, CIM, not periodic
times_m_5_not_periodic = [0.11115145683288574, 0.11257171630859375, 0.11686468124389648, 0.10946917533874512, 0.11298203468322754];

M = 8; # -> CIM
# With same gen, CIM, periodic
times_m_8_periodic = [0.06317996978759766, 0.06237983703613281, 0.06258487701416016, 0.06301450729370117, 0.06225132942199707];
# With same gen, CIM, not periodic
times_m_8_not_periodic = [0.05402517318725586, 0.05427074432373047, 0.05423927307128906, 0.054076433181762695, 0.05269312858581543];

M = 10; # -> CIM
# With same gen, CIM, periodic
times_m_10_periodic = [0.043503761291503906, 0.04454970359802246, 0.0451204776763916, 0.045270442962646484, 0.04576230049133301];
# With same gen, CIM, not periodic
times_m_10_not_periodic = [0.038770198822021484, 0.03910636901855469, 0.03928208351135254, 0.03941631317138672, 0.03973841667175293];

M = 13; # -> CIM
# With same gen, CIM, periodic
times_m_13_periodic = [0.03107142448425293, 0.03802180290222168, 0.03125643730163574, 0.03195452690124512, 0.03169870376586914];
# With same gen, CIM, not periodic
times_m_13_not_periodic = [0.028035402297973633, 0.0281064510345459, 0.028543949127197266, 0.02826094627380371, 0.028365373611450195];

figure('name', "Execution time with N = 1000, d=2.5 - Periodic active")
x_list = [2, 5, 8, 10, 13];
y_list = [mean(times_m_2_periodic), mean(times_m_5_periodic), mean(times_m_8_periodic), mean(times_m_10_periodic), mean(times_m_13_periodic)];
delta_y_list = [std(times_m_2_periodic), std(times_m_5_periodic), std(times_m_8_periodic), std(times_m_10_periodic), std(times_m_13_periodic)];
errorbar(x_list, y_list, delta_y_list)
title("tc = f(M)");
xlabel("M");
ylabel("tc [s]");

figure('name', "Execution time with N = 1000, d=2.5 - Periodic INactive")
y_list = [mean(times_m_2_not_periodic), mean(times_m_5_not_periodic), mean(times_m_8_not_periodic), mean(times_m_10_not_periodic), mean(times_m_13_not_periodic)];
delta_y_list = [std(times_m_2_not_periodic), std(times_m_5_not_periodic), std(times_m_8_not_periodic), std(times_m_10_not_periodic), std(times_m_13_not_periodic)];
errorbar(x_list, y_list, delta_y_list)
title("tc = f(M)");
xlabel("M");
ylabel("tc [s]");

############################################################################################################
# Take some M another N value.
# tc = f(M x M) With N = 200. M <= 13 because of condition
# Using onegen, same data for ALL, as previous results show similar values with more deviation
N = 200;

M = 2; # -> CIM
# With same gen, CIM, periodic
times_m_2_periodic = [0.03507494926452637, 0.034348487854003906, 0.03500676155090332, 0.033965110778808594, 0.034429073333740234];
# With same gen, CIM, not periodic
times_m_2_not_periodic = [0.01528477668762207, 0.01559305191040039, 0.015216588973999023, 0.015537500381469727, 0.015052556991577148];

M = 5; # -> CIM
# With same gen, CIM, periodic
times_m_5_periodic = [0.006663084030151367, 0.006910562515258789, 0.0067784786224365234, 0.006922006607055664, 0.0069522857666015625];
# With same gen, CIM, not periodic
times_m_5_not_periodic = [0.0054721832275390625, 0.005264997482299805, 0.0052721500396728516, 0.005248069763183594, 0.005315303802490234];

M = 8; # -> CIM
# With same gen, CIM, periodic
times_m_8_periodic = [0.0039348602294921875, 0.0037217140197753906, 0.003806591033935547, 0.0038344860076904297, 0.003838062286376953];
# With same gen, CIM, not periodic
times_m_8_not_periodic = [0.003251314163208008, 0.0032062530517578125, 0.0033006668090820312, 0.003279447555541992, 0.0032389163970947266];

M = 10; # -> CIM
# With same gen, CIM, periodic
times_m_10_periodic = [0.003107309341430664, 0.0031120777130126953, 0.003159046173095703, 0.0031626224517822266, 0.0031456947326660156];
# With same gen, CIM, not periodic
times_m_10_not_periodic = [0.002801179885864258, 0.0028984546661376953, 0.0029196739196777344, 0.0028162002563476562, 0.0028438568115234375];

M = 13; # -> CIM
# With same gen, CIM, periodic
times_m_13_periodic = [0.0027577877044677734, 0.0027942657470703125, 0.0027799606323242188, 0.0027005672454833984, 0.0027360916137695312];
# With same gen, CIM, not periodic
times_m_13_not_periodic = [0.0025818347930908203, 0.002571582794189453, 0.0025751590728759766, 0.002593994140625, 0.0026798248291015625];

figure('name', "Execution time with N = 200, d=0.5 - Periodic active")
x_list = [2, 5, 8, 10, 13];
y_list = [mean(times_m_2_periodic), mean(times_m_5_periodic), mean(times_m_8_periodic), mean(times_m_10_periodic), mean(times_m_13_periodic)];
delta_y_list = [std(times_m_2_periodic), std(times_m_5_periodic), std(times_m_8_periodic), std(times_m_10_periodic), std(times_m_13_periodic)];
errorbar(x_list, y_list, delta_y_list)
title("tc = f(M)");
xlabel("M");
ylabel("tc [s]");

figure('name', "Execution time with N = 200, d=0.5 - Periodic INactive")
y_list = [mean(times_m_2_not_periodic), mean(times_m_5_not_periodic), mean(times_m_8_not_periodic), mean(times_m_10_not_periodic), mean(times_m_13_not_periodic)];
delta_y_list = [std(times_m_2_not_periodic), std(times_m_5_not_periodic), std(times_m_8_not_periodic), std(times_m_10_not_periodic), std(times_m_13_not_periodic)];
errorbar(x_list, y_list, delta_y_list)
title("tc = f(M)");
xlabel("M");
ylabel("tc [s]");