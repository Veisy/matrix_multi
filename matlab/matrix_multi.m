clc;clear
%% Name: V. Y. YILMAZ
 % No: 194003062
 % This is the Homework 2 of the Introduction to Algorithm course,
 % implemented in MATLAB.

%% Enterance of the program

repeatMain = true;
while repeatMain
    % Menu
    disp('[1] Manuel Entrance')
    disp('[2] Random Entrance')
    disp('[3] Exit')
    menuInput = checkMenuInput();
    
    if menuInput == '3'
        repeatMain = false;
        
    elseif (menuInput == '1' || menuInput == '2')
        
        % First matrix dimensions are entered.
        [firstMatrixRow, firstMatrixCol] = enterMatrixDimensions ...
            ('Enter the ROW and COLUMN of FIRST MATRIX respectively :');
        
        % Repeat until valid matrix dimensions are given.
        notValid = true;
        while notValid
            % Ask for valid dimension for second matrix row. 
            % If not provided, ask again.
            secondMatrixRow = checkDimensionInput ... 
                ('Enter the ROW SECOND MATRIX :');
            
            % Check if matrix multiplication is possible.
            if (firstMatrixCol == secondMatrixRow)
                % Since matrix multiplication is possible, 
                % we can ask for second matrix column.
                secondMatrixCol = checkDimensionInput ...
                    ('Enter the COLUMN SECOND MATRIX :');
                
                notValid = false;
                disp('--------------------------------------')
                disp('The Matrix is Valid. Continue..')
                
                % Manual matrix entrance.
                if (menuInput == '1')
                    [firstMatrix, secondMatrix] = enterMatrices ...
                        (firstMatrixRow, firstMatrixCol, ...
                         secondMatrixRow, secondMatrixCol);
                     
                % Random matrices.
                else
                    [lowerBound, upperBound] = enterBounds();
                    [firstMatrix, secondMatrix] = randomMatrices ...
                        (firstMatrixRow, firstMatrixCol, ...
                         secondMatrixRow, secondMatrixCol, ...
                         lowerBound, upperBound);
                end
                
                resultMatrix = matrixMultiplication ...
                    (firstMatrix, secondMatrix);
                printMatrix('RESULT MATRIX: ', resultMatrix)
                
            else
                disp('Invalid calculation!')
                disp('The column of column of first matrix have to be ')
                disp('equal to row of the second matrix!')
                disp('--------------------------------------')
                disp('')
            end
        end
    end
end


%% Functions are defined below.

% Functions with '_' at the end of their names are functions that 
% are not used directly, but only used by other functions.


function resultMatrix = matrixMultiplication(firstMatrix, secondMatrix)
    % Initialize result matrix with empty fields.
    resultMatrix = zeros(size(firstMatrix, 1), size(secondMatrix, 2));
    
    % Loop over first matrix's row and second matrix's column.
    for i = 1:size(firstMatrix, 1)
        for j = 1:size(secondMatrix, 2)
            % Multiply the values in the row of the first matrix 
            % with the values in the column of the second matrix,
            % and add them all.
            % Then save this value to the row and column index of the result matrix.
            multipliedValue = 0;
            for k = 1:size(secondMatrix, 1)
                multipliedValue = multipliedValue ...
                    + firstMatrix(i,k) * secondMatrix(k,j);
                
            resultMatrix(i,j) = multipliedValue;
            end
        end
    end
end


% Check keyboard inputs for main menu, dimensions and matrix data.
function stringInput = checkMenuInput
    while true
        stringInput = input('', 's');
        try
            if (stringInput ~= '1' ...
                && stringInput ~= '2' ...
                && stringInput ~= '3')
            
               throw(MException('MATLAB:invalidMenuInput', ...
                   'Invalid menu selection.'))
            end
            
            break
        catch
            disp('Please enter a number between 1-3');
        end
    end      
end


function doubleInput = checkDoubleInput_(message)
    disp(message)
    while true
        stringInput = input('', 's');
        try
            doubleInput = str2double(stringInput);
            if (isnan(doubleInput))
                throw(MException('MATLAB:invalidDoubleInput', ...
                    'Invalid input, expected double.'))
            end
            break
        catch
            disp('Please enter a number.')
        end
    end
end


function numInput = checkDimensionInput(message)
    disp(message)
    while true
        try
            numInput = checkDoubleInput_('');
            if (~(isinf(numInput)) && (floor(numInput) == numInput))
                if  numInput > 0 && numInput <= 100
                    break
                end
                disp('Supported dimension values are between 1-100.')
            else
                disp('Enter a integer value')
            end
        catch
            disp('Please enter a valid dimension.')
        end
    end
end


function [row, column] = enterMatrixDimensions(message)
    disp(message)
    row = checkDimensionInput('');
    column = checkDimensionInput('');
end


function singleMatrix = enterMatrixData_(message, rows, cols)
    disp(message)
    singleMatrix = zeros(rows, cols);
    
    for i = 1:rows
        for j = 1:cols
            fprintf('[%d][%d]: ', i, j)
            singleMatrix(i, j) = checkDoubleInput_('');
        end
    end
    printMatrix(message, singleMatrix)
end


function [firstMatrix, secondMatrix] = enterMatrices ...
    (firstMatrixRow, firstMatrixCol, ...
     secondMatrixRow, secondMatrixCol)
              
    firstMatrix = enterMatrixData_('FIRST MATRIX : ', ...
        firstMatrixRow, firstMatrixCol);
    
    secondMatrix = enterMatrixData_('SECOND MATRIX : ', ...
        secondMatrixRow, secondMatrixCol);
end


% Check if lower bound is smaller then upper bound. If not, ask again.
function [lowerBound, upperBound] = enterBounds
    while true
        lowerBound = checkDoubleInput_('Enter lower bound: ');
        upperBound = checkDoubleInput_('Enter upper bound: ');
        if lowerBound < upperBound
            break
        end
        disp('Upper bound must be bigger than lower bound.')

    end
end


function singleMatrix = randomMatriceData_ ...
    (message, rows, cols, lowerBound, upperBound)
    
    singleMatrix = zeros(rows, cols);
    
    for i = 1:rows
        for j = 1:cols
            singleMatrix(i, j) = randi([lowerBound, upperBound]);
        end
    end
    printMatrix(message, singleMatrix)
end


function [firstMatrix, secondMatrix] = randomMatrices ...
    (firstMatrixRow, firstMatrixCol, ...
     secondMatrixRow, secondMatrixCol, ...
     lowerBound, upperBound)
    
    firstMatrix = randomMatriceData_("FIRST MATRIX : ", ...
        firstMatrixRow, firstMatrixCol, lowerBound, upperBound);
    
    secondMatrix = randomMatriceData_("SECOND MATRIX : ", ...
        secondMatrixRow, secondMatrixCol, lowerBound, upperBound);
end
    

function printMatrix(message, matrix)
    disp(' ')
    disp(message)
    disp('-----------')
    for i = 1:size(matrix, 1)
        for j = 1:size(matrix, 2)
            fprintf('%d ', matrix(i, j))
        end
        disp(' ')
    end
    disp(' ')
end





        
            


       
        




         
    