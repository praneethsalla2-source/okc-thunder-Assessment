import {
  ChangeDetectorRef,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation
} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {untilDestroyed, UntilDestroy} from '@ngneat/until-destroy';
import {PlayersService} from '../_services/players.service';
import {PlayerSummary, PlayerSummaryResponse} from '../_models/player-summary.interface';

@UntilDestroy()
@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class PlayerSummaryComponent implements OnInit, OnDestroy {
  playerSummary: PlayerSummary | null = null;
  loading = true;
  error: string | null = null;

  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected playersService: PlayersService,
  ) {

  }

  ngOnInit(): void {
    // Get player ID from route params or default to 0
    const playerId = this.activatedRoute.snapshot.params['playerID'] || 0;
    
    this.playersService.getPlayerSummary(parseInt(playerId)).pipe(untilDestroyed(this)).subscribe({
      next: (response: PlayerSummaryResponse) => {
        this.playerSummary = response.apiResponse;
        this.loading = false;
        this.error = null;
        this.cdr.detectChanges();
      },
      error: (err) => {
        this.error = 'Failed to load player summary';
        this.loading = false;
        this.cdr.detectChanges();
        console.error('Error loading player summary:', err);
      }
    });
  }

  ngOnDestroy() {
  }

}