% Create data matrix
data_1 = [0.614798364	0.631746614	0.64821694	0.665338531	...	0.965967175];

% Creating x, y axis coordinate vectors
x = 0.01 * [0:19] + 0.8;
y = [1, 0.5, 0.33333];

set(gca, 'FontName', 'Times New Roman');
set(groot, 'DefaultAxesFontName', 'Times New Roman');
% Visualize using the surf function.
colormap summer;
colormap(flipud(summer)); % Setting Colors
contourf(x, y, data_1, 'LineColor','none');
xlabel('Precipitation ratio', 'FontSize', 12);
ylabel('Frequency', 'interpreter', 'latex', 'FontSize', 12);
title('Fertility factor of the fifth year(1 population)', 'FontSize', 16);
caxis([0.6, 1.3])
colorbar;
% Get the handle of the current colorbar
cb = colorbar;
% Set the upper and lower labels of the colorbar
axesPosition = cb.Position;
axes('Position', axesPosition, 'Visible', 'off');
% Add labels to an axis object
text(3.5, -0.02, 'withered', 'HorizontalAlignment', 'center', 'FontSize', 11);
text(3.5, 0.98, 'luxuriant', 'HorizontalAlignment', 'center', 'FontSize', 11);
