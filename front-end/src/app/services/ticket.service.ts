import { HttpClient } from '@angular/common/http';
import { inject, Service } from '@angular/core';
import { Observable } from 'rxjs';
import { TicketResposta } from '../layout/navbar/models/ticket.model';

@Service()
export class TicketService {

    // httpclient é o cliente que utilizamos no angular para fazer requests
    private http = inject(HttpClient);

    // url do back por enquanto é fixo, depois utilizaremos environment para ser dinâmico
    private baseUrl = `http://localhost:8000/tickets`

    // fnucao que sera responsavel por comunicar com o back para obter lista de tickets
    listar(): Observable<TicketResposta[]>{
        return this.http.get<TicketResposta[]>(this.baseUrl);
    }
}
