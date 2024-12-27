        // Variables globales
        let subtotal_horarioregular = 0;
        let subtotal_horarioextendido = 0;
        let entrada_total = 0;
    
        let Var_Participantes_hijos = '';
        let Var_Participantes_amigos = '';
        let Var_Participantes_amigos2 = 0;
        let Dias_Seleccionados = 0;
        let Total_Participantes = 0;
        let displayMethod = "Efectivo"; // Valor inicial
    
        // Función para actualizar el total a pagar
        function updateTotalApagar() {
            const horarioExtra = parseFloat(document.getElementById("horario_extra").textContent) || 0;
            const subtotalHorarioRegular = parseFloat(subtotal_horarioregular) || 0;
            const totalApagar = horarioExtra + subtotalHorarioRegular;
    
        // Format the total amount with commas separating thousands
            const formattedTotalApagar = totalApagar.toLocaleString('en-US', {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
            });

            // Set the formatted total amount to the element
            const totalApagarElement = document.getElementById("TotalApagar");
            totalApagarElement.textContent = `Total a Pagar: $${formattedTotalApagar}`;

            // Change the background color to blue
            totalApagarElement.style.backgroundColor = "rgb(182, 5, 206)";
            // Change the text color to white for better readability
            totalApagarElement.style.color = 'white';

            // Ensure padding and text alignment for better visibility
            totalApagarElement.style.padding = '5px';
            totalApagarElement.style.textAlign = 'center';
        }
        
        // Función para actualizar los días seleccionados
        function updateDiasSeleccionados() {
            document.getElementById("Label_Dias_Seleccionados").textContent = Dias_Seleccionados;
            updateSubtotalHorarioregular();
        }
    
        
        // Función para actualizar el subtotal de horario regular
        function updateSubtotalHorarioregular() {
            const diasSeleccionados = Dias_Seleccionados;
            const participantesHijos = parseInt(Var_Participantes_hijos) || 0;
    
            let valor = 0;
            let participantesAux = participantesHijos;

            if (participantesHijos == 1) {
                if (Var_Participantes_amigos2 == 1) {
                    participantesAux = 2; // Corrección: Usar '=' en lugar de '=='
                }
            }


            if (diasSeleccionados >= 1 && diasSeleccionados <= 4) {
                valor = displayMethod === "Efectivo" ?
                    (participantesAux === 1 ? 305 : participantesAux  === 2 ? 285 : 260) :
                    (participantesAux  === 1 ? 305 : participantesAux  === 2 ? 285 : 260);
            } else if (diasSeleccionados >= 5 && diasSeleccionados <= 9) {
                valor = displayMethod === "Efectivo" ?
                    (participantesAux  === 1 ? 288 : participantesAux  === 2 ? 265 : 253) :
                    (participantesAux  === 1 ? 288 : participantesAux  === 2 ? 265 : 253);
            } else if (diasSeleccionados >= 10 && diasSeleccionados <= 14) {
                valor = displayMethod === "Efectivo" ?
                    (participantesAux  === 1 ? 273 : participantesAux  === 2 ? 251 : 241) :
                    (participantesAux  === 1 ? 280 : participantesAux  === 2 ? 262 : 251);
            } else if (diasSeleccionados >= 15 && diasSeleccionados <= 18) {
                valor = displayMethod === "Efectivo" ?
                    (participantesAux  === 1 ? 265 : participantesAux  === 2 ? 245 : 234) :
                    (participantesAux  === 1 ? 276 : participantesAux  === 2 ? 260 : 249);
            }

             
    
            subtotal_horarioregular = valor * diasSeleccionados * (participantesHijos + Var_Participantes_amigos2);
            document.getElementById("subtotal_horarioregular").textContent = subtotal_horarioregular.toFixed(2);
            updateTotalApagar();
        }
    
        document.getElementById("payment-method").addEventListener("change", function () {
            displayMethod = this.value === "credit-card" ? "Tarjeta de crédito" : "Efectivo";
            updateSubtotalHorarioregular();
        });
    
        document.querySelectorAll('.calendar td').forEach(cell => {
            if (!cell.classList.contains('disabled') && cell.innerText.trim() !== "") {
                const span = cell.querySelector('span'); // Get the span inside the cell
                cell.addEventListener('click', () => {
                    if (!span.classList.contains('selected')) {
                        span.classList.add('selected');
                        Dias_Seleccionados++;
                    } else {
                        span.classList.remove('selected');
                        Dias_Seleccionados--;
                    }
                    updateDiasSeleccionados();
                });
            }
        });
    
        document.getElementById('Participantes_hijos').addEventListener('change', function () {
            updateTotalParticipantes();
        });
    
        document.getElementById('checkbox_primo').addEventListener('change', function () {
            updateTotalParticipantes();
        });
    
        function updateTotalParticipantes() {
            const selectParticipantesHijos = document.getElementById('Participantes_hijos');
            const checkboxPrimo = document.getElementById('checkbox_primo');
            const totalParticipantesLabel = document.getElementById('totalParticipantesLabel');
    
            let participantesHijos = parseInt(selectParticipantesHijos.value) || 0;

            if (participantesHijos = parseInt(selectParticipantesHijos.value) || 0){
                checkbox_primo.disabled = false;
            }
    
            if (checkboxPrimo.checked) {
                Var_Participantes_amigos2 = 1;
            } else {
                Var_Participantes_amigos2 = 0;
            }
    
            totalParticipantesLabel.textContent = participantesHijos + Var_Participantes_amigos2;
            Var_Participantes_hijos = participantesHijos.toString();
            updateSubtotalHorarioregular();
        }
    
        document.getElementById('Participantes_amigos').addEventListener('change', function() {
            Var_Participantes_amigos = this.value;
        });


// Global variables to store state


// Llama a updateHorarioExtra cuando cambian las condiciones relevantes
document.getElementById('Participantes_hijos').addEventListener('change', updateHorarioExtra);
document.getElementById("8am").addEventListener("change", updateHorarioExtra);
document.getElementById("8am-pa1").addEventListener("change", updateHorarioExtra);
document.getElementById("2pm").addEventListener("change", updateHorarioExtra);
document.getElementById("2pm-pa1").addEventListener("change", updateHorarioExtra);
document.getElementById("3pm").addEventListener("change", updateHorarioExtra);
document.getElementById("3pm-pa1").addEventListener("change", updateHorarioExtra);
document.querySelectorAll('.calendar td').forEach(cell => {
cell.addEventListener('click', updateHorarioExtra);
});
