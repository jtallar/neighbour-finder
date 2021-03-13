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

N = 1000;
# With same gen, optimal M = 13
times_1000_onegen = [0.03317117691040039, 0.033503055572509766, 0.03279733657836914, 0.03285408020019531, 0.03364157676696777];
# With different gens, optimal M = 13
times_1000_multigen = [0.032028913497924805, 0.032148122787475586, 0.032517194747924805, 0.03147411346435547, 0.03451371192932129];

x_list = [100, 300, 500, 700, 1000];
y_list = [mean(times_100_onegen), mean(times_300_onegen), mean(times_500_onegen), mean(times_700_onegen), mean(times_1000_onegen)];
delta_y_list = [std(times_100_onegen), std(times_300_onegen), std(times_500_onegen), std(times_700_onegen), std(times_1000_onegen)];
errorbar(x_list, y_list, delta_y_list)
title("Execution time with M = 13 (optimal M?) - One generator");
xlabel("N");
ylabel("tc [s]");

figure(2)
y_list = [mean(times_100_multigen), mean(times_300_multigen), mean(times_500_multigen), mean(times_700_multigen), mean(times_1000_multigen)];
delta_y_list = [std(times_100_multigen), std(times_300_multigen), std(times_500_multigen), std(times_700_multigen), std(times_1000_multigen)];
errorbar(x_list, y_list, delta_y_list)
title("Execution time with M = 13 (optimal M?) - Multiple generators");
xlabel("N");
ylabel("tc [s]");