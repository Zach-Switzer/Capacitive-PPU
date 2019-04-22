clear all; 
close all;
clc;

%% Total Resistance = 125 ohms

% Take data from excel file => will be stored as a "table"
O = readtable('C:\Users\Zach\Documents\Research\Thesis\Capacitor Charging.xlsx', 'Sheet',1, 'Range','O4:O629');
T = readtable('C:\Users\Zach\Documents\Research\Thesis\Capacitor Charging.xlsx', 'Sheet',1, 'Range','T4:T629');

% circuit info
R=125; % resistance | ESR [ohms]
C=0.01e-6; % capacitance [uF]
TC=5*R*C; % time constant | time to capacitor full charge [s]

% manipulate data
time=table2array(O)'; % convert the table to an array to use the data
voltage=table2array(T)';
area_cap=trapz(time,voltage); % area under the voltage vs time curve
V_PW=[0, 200e-9]; % voltage spike pulse width time [s]
V_spike=[1.06e3, 1.06e3]; % voltage spike voltage [V]
area_spike=trapz(V_PW, V_spike); % area under the voltage spike curve
pulses=area_cap/area_spike; % number of pulses needed to fully charge capacitor
freq=5; % frequency sent to the IGBT [Hz]
period=1/freq; % [s]
tot_charge=pulses*period; % real-time needed to charge capacitor [s]
safe_charge=tot_charge*.65; % safe cutoff time to charge capacitor [s]
safe_pulses=round(safe_charge/period,0); % number of pulses for safe cutoff time
safe_cap_time=200e-9*safe_pulses; % time capacitor is charging [s]

fprintf('The pulse width of a 1kV Voltage Spike:\n%d [ns] \n\n', V_PW(2)*1e9)
fprintf('The time needed to fully charge a 0.01uF capacitor to 1kV:\n%f [us] \n\n', TC*1e6)
fprintf('The number of pulses needed for a fully charged capacitor:\n%i \n\n', round(pulses,0))
fprintf('The switching frequency on the IGBT:\n%i [Hz] \n\n', freq)
fprintf('The "real" time to charge:\n%f [s] \n\n', period*round(pulses,0))
fprintf('The safe cuttoff time:\n%f [s] \n\n', safe_charge)
fprintf('The number of pulses (with a FOS):\n%i \n\n', safe_pulses)
fprintf('How much charge time the capacitor sees (with a FOS):\n%f [us] \n\n', safe_cap_time*1e6)

%plot it
figure;
plot(time,voltage,'r')
hold on;
plot([safe_cap_time, safe_cap_time],[0, 1.2e3], 'b')
title('Voltage vs Time: R=125ohms')
xlabel('Time [s]')
ylabel('Voltage [V]')
legend('show','Location','southeast');
legend('Ideal Capacitive Storage', 'Safe Cutoff Time')

%% Manually-Entered Data
% v=[0 7e-8 1.5e-7 2.2e-7 3.5e-7 5.1e-7 6.6e-7 8.4e-7 1.1e-6 1.38e-6 ...
%     1.75e-6 2.04e-6 2.25e-6 2.6e-6 3.07e-6 3.4e-6 3.8e-6 4.1e-6 ...
%     4.45e-6 4.8e-6 5.15e-6];
% f=[0 6.54e1 1.36e2 1.94e2 2.93e2 4.02e2 4.92e2 5.87e2 7.02e2 8.02e2 ...
%     9.04e2 9.65e2 1e3 1.05e3 1.1e3 1.12e3 1.14e3 1.15e3 1.17e3 ...
%     1.17e3 1.18e3];
% len=length(f)/length(v); %show that the lengths are the same