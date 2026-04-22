const tableBody = document.getElementById('team-table-body');
const backendStatus = document.getElementById('backend-status');


fetch('http://localhost:5000/api/team')
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la red');
        }
        
        backendStatus.textContent = 'Online';
        backendStatus.className = 'online';
        return response.json();
    })
    .then(data => {
       
        data.forEach(member => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${member.nombre}</td>
                <td>${member.legajo}</td>
                <td>${member.feature}</td>
                <td>${member.servicio}</td>
                <td>${member.estado}</td>
            `;
            tableBody.appendChild(row);
        });
    })
    .catch(error => {
        console.error('Error al obtener los datos:', error);
        
        backendStatus.textContent = 'Offline (Error de conexión)';
        backendStatus.className = 'offline';
    });